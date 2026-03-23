"""
charts.py
---------
Matplotlib/Seaborn chart builders for MoneyMind.

Each function accepts a processed DataFrame and returns a Matplotlib Figure.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
from matplotlib.figure import Figure
from matplotlib.patches import Wedge

from utils import (
    CHART_PALETTE,
    C_TEXT,
    C_TEXT_MUT,
    C_POSITIVE,
    C_NEGATIVE,
    C_ACCENT,
    C_WARNING,
)
from data_processing import (
    category_spending,
    monthly_spending_trend,
    top_expense_categories,
    day_of_week_spending,
    monthly_category_heatmap_data,
)


_dark: bool = False


def set_dark(dark: bool) -> None:
    """Update chart theme mode used by all figure builders."""
    global _dark
    _dark = dark


def _theme() -> dict[str, str]:
    if _dark:
        return {
            "bg": "#1E293B",
            "fg": C_TEXT,
            "muted": C_TEXT_MUT,
            "grid": "#334155",
        }
    return {
        "bg": "#FFFFFF",
        "fg": "#0F172A",
        "muted": "#475569",
        "grid": "#E2E8F0",
    }


def _new_figure(width: float = 8.0, height: float = 3.8) -> tuple[Figure, plt.Axes]:
    t = _theme()
    fig, ax = plt.subplots(figsize=(width, height), dpi=120)
    fig.patch.set_facecolor(t["bg"])
    ax.set_facecolor(t["bg"])
    return fig, ax


def _style_axes(ax: plt.Axes, x_label: str = "", y_label: str = "") -> None:
    t = _theme()
    ax.set_xlabel(x_label, color=t["muted"], fontsize=10)
    ax.set_ylabel(y_label, color=t["muted"], fontsize=10)
    ax.tick_params(colors=t["muted"], labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(t["grid"])
    ax.grid(axis="y", color=t["grid"], alpha=0.45, linewidth=0.7)
    ax.set_axisbelow(True)


def fig_spending_pie(df: pd.DataFrame) -> Figure:
    cat_df = category_spending(df).head(10)
    fig, ax = _new_figure(width=8.6, height=4.8)
    t = _theme()
    if cat_df.empty:
        ax.text(0.5, 0.5, "No spending data", ha="center", va="center", color=t["muted"])
        ax.axis("off")
        return fig

    colors = CHART_PALETTE[: len(cat_df)]
    values = cat_df["total_spent"].to_numpy(dtype=float)

    wedges, _texts, _autotexts = ax.pie(
        values,
        labels=None,
        autopct=lambda p: f"{p:.1f}%" if p >= 2 else "",
        startangle=120,
        colors=colors,
        radius=1.10,
        wedgeprops={"width": 0.45, "edgecolor": t["bg"]},
        textprops={"color": t["fg"], "fontsize": 8},
        pctdistance=0.72,
    )

    label_points: list[dict[str, float | int]] = []
    for i, wedge in enumerate(wedges):
        angle = np.deg2rad((wedge.theta1 + wedge.theta2) / 2.0)
        x = float(np.cos(angle))
        y = float(np.sin(angle))
        side = 1 if x >= 0 else -1
        label_points.append({"idx": i, "x": x, "y": y, "side": side, "y_text": 1.18 * y})

    for side in (-1, 1):
        side_points = sorted(
            [p for p in label_points if p["side"] == side],
            key=lambda p: float(p["y_text"]),
        )
        min_gap = 0.14
        for j in range(1, len(side_points)):
            prev_y = float(side_points[j - 1]["y_text"])
            cur_y = float(side_points[j]["y_text"])
            if cur_y - prev_y < min_gap:
                side_points[j]["y_text"] = prev_y + min_gap

        if side_points:
            y_top = float(side_points[-1]["y_text"])
            y_bottom = float(side_points[0]["y_text"])
            if y_top > 1.22:
                shift = y_top - 1.22
                for p in side_points:
                    p["y_text"] = float(p["y_text"]) - shift
            if y_bottom < -1.22:
                shift = -1.22 - y_bottom
                for p in side_points:
                    p["y_text"] = float(p["y_text"]) + shift

    for p in label_points:
        i = int(p["idx"])
        side = int(p["side"])
        x = float(p["x"])
        y = float(p["y"])
        y_text = float(p["y_text"])
        ax.annotate(
            textwrap.fill(str(cat_df["category"].iloc[i]), width=14),
            xy=(0.98 * x, 0.98 * y),
            xytext=(1.48 * side, y_text),
            ha="left" if side > 0 else "right",
            va="center",
            fontsize=8,
            color=t["fg"],
            arrowprops={
                "arrowstyle": "-",
                "color": t["muted"],
                "lw": 0.9,
                "shrinkA": 0,
                "shrinkB": 0,
                "connectionstyle": "arc3,rad=0",
            },
        )

    total = cat_df["total_spent"].sum()
    ax.text(0, 0, f"₹{total:,.0f}", ha="center", va="center", color=t["fg"], fontsize=12, fontweight="bold")
    ax.set_xlim(-1.88, 1.88)
    ax.set_ylim(-1.35, 1.35)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.97, bottom=0.06)
    ax.axis("equal")
    return fig


def fig_treemap(df: pd.DataFrame) -> Figure:
    cat_df = category_spending(df).head(10).sort_values("total_spent")
    fig, ax = _new_figure(height=3.4)
    if cat_df.empty:
        ax.text(0.5, 0.5, "No spending data", ha="center", va="center", color=_theme()["muted"])
        ax.axis("off")
        return fig

    sns.barplot(
        data=cat_df,
        x="total_spent",
        y="category",
        palette=sns.color_palette("Blues", n_colors=len(cat_df)),
        ax=ax,
    )
    _style_axes(ax, x_label="Total Spent (₹)", y_label="")
    ax.set_title("Category Distribution", color=_theme()["fg"], fontsize=11, pad=10)
    return fig


def fig_top_categories(df: pd.DataFrame) -> Figure:
    top = top_expense_categories(df, top_n=10).sort_values("total_spent")
    fig, ax = _new_figure(height=3.4)
    if top.empty:
        ax.text(0.5, 0.5, "No category data", ha="center", va="center", color=_theme()["muted"])
        ax.axis("off")
        return fig

    bars = ax.barh(top["category"], top["total_spent"], color=C_ACCENT, alpha=0.85)
    for bar, value in zip(bars, top["total_spent"]):
        ax.text(value, bar.get_y() + bar.get_height() / 2, f" ₹{value:,.0f}", va="center", color=_theme()["muted"], fontsize=8)
    _style_axes(ax, x_label="Total Spent (₹)", y_label="")
    return fig


def fig_day_of_week(df: pd.DataFrame) -> Figure:
    dow = day_of_week_spending(df)
    fig, ax = _new_figure(height=3.4)
    if dow.empty:
        ax.text(0.5, 0.5, "No day-wise data", ha="center", va="center", color=_theme()["muted"])
        ax.axis("off")
        return fig

    ax.bar(dow["day_of_week"], dow["total_spent"], color=C_ACCENT, alpha=0.9)
    _style_axes(ax, x_label="", y_label="Total Spent (₹)")
    ax.tick_params(axis="x", rotation=25)
    return fig


def fig_monthly_trend(df: pd.DataFrame) -> Figure:
    m = monthly_spending_trend(df)
    fig, ax = _new_figure(height=3.8)
    if m.empty:
        ax.text(0.5, 0.5, "No monthly trend data", ha="center", va="center", color=_theme()["muted"])
        ax.axis("off")
        return fig

    x = np.arange(len(m))
    ax.bar(x, m["net_balance"], color=[C_POSITIVE if v >= 0 else C_NEGATIVE for v in m["net_balance"]], alpha=0.25, label="Net Balance")
    ax.plot(x, m["total_income"], color=C_POSITIVE, marker="o", linewidth=2, label="Income")
    ax.plot(x, m["total_spending"], color=C_NEGATIVE, marker="o", linewidth=2, label="Expenses")

    # Keep peaks from touching the top boundary when values spike.
    y_vals = np.concatenate([
        m["net_balance"].to_numpy(dtype=float),
        m["total_income"].to_numpy(dtype=float),
        m["total_spending"].to_numpy(dtype=float),
        np.array([0.0]),
    ])
    y_min = float(np.nanmin(y_vals))
    y_max = float(np.nanmax(y_vals))
    y_span = max(y_max - y_min, 1.0)
    pad = 0.20 * y_span
    ax.set_ylim(y_min - pad, y_max + pad)

    # Limit shown month labels so they remain readable on dense timelines.
    step = max(1, int(np.ceil(len(m) / 12)))
    tick_idx = np.arange(0, len(m), step)
    if tick_idx[-1] != len(m) - 1:
        tick_idx = np.append(tick_idx, len(m) - 1)

    ax.set_xticks(tick_idx)
    ax.set_xticklabels(m["month_label"].iloc[tick_idx], rotation=28, ha="right", fontsize=8)
    _style_axes(ax, x_label="", y_label="Amount (₹)")
    leg = ax.legend(frameon=False, fontsize=7)
    for txt in leg.get_texts():
        txt.set_color(_theme()["muted"])
    # Extra bottom room for rotated date labels.
    fig.subplots_adjust(bottom=0.28, top=0.96, left=0.09, right=0.98)
    return fig


def fig_cumulative_balance(df: pd.DataFrame) -> Figure:
    df_s = df.sort_values("date").copy()
    fig, ax = _new_figure(height=3.0)
    if df_s.empty:
        ax.text(0.5, 0.5, "No balance data", ha="center", va="center", color=_theme()["muted"])
        ax.axis("off")
        return fig

    df_s["cumulative"] = df_s["signed_amount"].cumsum()
    ax.plot(df_s["date"], df_s["cumulative"], color=C_ACCENT, linewidth=2)
    ax.fill_between(df_s["date"], df_s["cumulative"], 0, color=C_ACCENT, alpha=0.15)
    _style_axes(ax, x_label="", y_label="Balance (₹)")
    return fig


def fig_heatmap(df: pd.DataFrame) -> Figure:
    hm = monthly_category_heatmap_data(df)
    fig, ax = _new_figure(width=9.2, height=4.4)
    if hm.empty:
        ax.text(0.5, 0.5, "No heatmap data", ha="center", va="center", color=_theme()["muted"])
        ax.axis("off")
        return fig

    if hm.shape[1] > 24:
        hm = hm.iloc[:, -24:]

    cmap = sns.color_palette("Blues", as_cmap=True)
    sns.heatmap(hm, ax=ax, cmap=cmap, linewidths=0.3, linecolor=_theme()["grid"], cbar=True)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="x", colors=_theme()["muted"], labelrotation=45, labelsize=8)
    ax.tick_params(axis="y", colors=_theme()["fg"], labelsize=8)
    return fig


def fig_savings_gauge(gauge_val: float, target: float) -> Figure:
    fig, ax = _new_figure(width=7.2, height=3.0)
    gauge_val = max(0.0, min(100.0, float(gauge_val)))
    target = max(0.0, min(100.0, float(target)))
    t = _theme()

    if gauge_val >= target:
        bar_color = C_POSITIVE
    elif gauge_val >= target * 0.7:
        bar_color = C_WARNING
    else:
        bar_color = C_NEGATIVE

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-0.15, 1.15)
    ax.set_aspect("equal")
    ax.axis("off")

    outer_r = 1.0
    width = 0.22

    # Base ring
    bg_ring = Wedge((0, 0), r=outer_r, theta1=0, theta2=180, width=width,
                    facecolor=t["grid"], alpha=0.45, edgecolor="none")
    ax.add_patch(bg_ring)

    # Filled progress arc
    value_end = 180 - (gauge_val / 100.0) * 180.0
    val_ring = Wedge((0, 0), r=outer_r, theta1=value_end, theta2=180, width=width,
                     facecolor=bar_color, alpha=0.95, edgecolor="none")
    ax.add_patch(val_ring)

    # Target marker
    tgt_angle = np.deg2rad(180 - (target / 100.0) * 180.0)
    x0, y0 = (outer_r - width - 0.03) * np.cos(tgt_angle), (outer_r - width - 0.03) * np.sin(tgt_angle)
    x1, y1 = (outer_r + 0.02) * np.cos(tgt_angle), (outer_r + 0.02) * np.sin(tgt_angle)
    ax.plot([x0, x1], [y0, y1], color=t["muted"], linewidth=1.8)

    # Tick labels
    for tick in [0, 20, 40, 60, 80, 100]:
        ang = np.deg2rad(180 - (tick / 100.0) * 180.0)
        xt, yt = 1.07 * np.cos(ang), 1.07 * np.sin(ang)
        ax.text(xt, yt, f"{tick}%", ha="center", va="center", color=t["muted"], fontsize=7)

    # Title + center stats
    ax.text(0, 0.92, "Savings Rate", ha="center", va="center", color=t["muted"], fontsize=9)
    ax.text(0, 0.26, f"{gauge_val:.1f}%", ha="center", va="center", color=t["fg"], fontsize=22, fontweight="bold")
    delta = gauge_val - target
    delta_col = C_POSITIVE if delta >= 0 else C_NEGATIVE
    delta_sym = "+" if delta >= 0 else ""
    ax.text(0, 0.10, f"{delta_sym}{delta:.1f}%", ha="center", va="center", color=delta_col, fontsize=11)

    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.06, top=0.96)
    return fig
