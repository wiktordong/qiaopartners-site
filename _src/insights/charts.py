"""Small SVG chart helpers. Every colour is a CSS token so exhibits follow the page theme."""
from datetime import date
from html import escape

W = 760


def _svg(h, label, body):
    return (f'<svg viewBox="0 0 {W} {h}" role="img" aria-label="{escape(label)}" '
            f'class="ex-svg" font-family="var(--f-data)" font-size="12">{body}</svg>')


def fmt(v, dec=0):
    return f"{v:,.{dec}f}"


def bars(rows, label, unit="", highlight=None, dec=0, h=300):
    """Vertical bars from zero. rows = [(label, value)]; highlight = index drawn in accent."""
    left, right, y0, base = 24, W - 24, 30, h - 40
    peak = max(v for _, v in rows) * 1.12
    band = (right - left) / len(rows)
    bw = min(64, band * 0.6)
    out = [f'<line x1="{left}" x2="{right}" y1="{base}" y2="{base}" stroke="var(--rule-strong)"/>']
    for i, (lab, v) in enumerate(rows):
        x = left + i * band + (band - bw) / 2
        y = base - v / peak * (base - y0)
        acc = (highlight == i) or (highlight == -1 and i == len(rows) - 1)
        fill = "var(--accent)" if acc else "var(--ex-mute)"
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{base - y:.1f}" fill="{fill}">'
                   f'<title>{escape(lab)}: {fmt(v, dec)}{unit}</title></rect>')
        out.append(f'<text x="{x + bw / 2:.1f}" y="{y - 8:.1f}" text-anchor="middle" fill="var(--ink)" '
                   f'font-weight="{600 if acc else 400}">{fmt(v, dec)}{unit}</text>')
        out.append(f'<text x="{x + bw / 2:.1f}" y="{base + 20}" text-anchor="middle" fill="var(--muted)">{escape(lab)}</text>')
    return _svg(h, label, "".join(out))


def line(points, label, unit="", h=320, notes=(), month_fmt=None):
    """Time series. points = [(date, value, label_or_None)]; notes = [(date, text)] vertical markers."""
    left, right, y0, base = 56, W - 30, 26, h - 44
    d0, d1 = points[0][0].toordinal(), points[-1][0].toordinal()
    vmax = max(v for _, v, _ in points) * 1.12
    X = lambda d: left + (d.toordinal() - d0) / (d1 - d0) * (right - left)
    Y = lambda v: base - v / vmax * (base - y0)
    out = []
    step = 20 if vmax > 60 else 10
    t = 0
    while t <= vmax:
        out.append(f'<line x1="{left}" x2="{right}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="var(--rule)"/>'
                   f'<text x="{left - 8}" y="{Y(t) + 4:.1f}" text-anchor="end" fill="var(--muted)">{t}</text>')
        t += step
    for d, txt in notes:
        x = X(d)
        out.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{y0}" y2="{base}" stroke="var(--muted)" stroke-dasharray="3 4"/>'
                   f'<text x="{x + 6:.1f}" y="{y0 + 12}" fill="var(--muted)">{escape(txt)}</text>')
    path = " ".join(f'{"M" if i == 0 else "L"}{X(d):.1f},{Y(v):.1f}' for i, (d, v, _) in enumerate(points))
    out.append(f'<path d="{path}" fill="none" stroke="var(--accent)" stroke-width="2.25"/>')
    for d, v, lab in points:
        out.append(f'<circle cx="{X(d):.1f}" cy="{Y(v):.1f}" r="3.5" fill="var(--accent)">'
                   f'<title>{d.strftime("%d %b %Y")}: {fmt(v, 1)}{unit}</title></circle>')
        if lab:
            out.append(f'<text x="{X(d):.1f}" y="{Y(v) - 10:.1f}" text-anchor="middle" fill="var(--ink)" font-weight="600">{escape(lab)}</text>')
    # month ticks at quarter starts
    for (yy, mm) in [(2025, 10), (2026, 1), (2026, 4), (2026, 7), (2026, 10)]:
        d = date(yy, mm, 1)
        if d0 <= d.toordinal() <= d1:
            out.append(f'<text x="{X(d):.1f}" y="{base + 20}" text-anchor="middle" fill="var(--muted)">{month_fmt(d) if month_fmt else d.strftime("%b %y")}</text>')
    out.append(f'<line x1="{left}" x2="{right}" y1="{base}" y2="{base}" stroke="var(--rule-strong)"/>')
    return _svg(h, label, "".join(out))


def stack(segments, target, label, unit="", h=170, target_label="Target", dec=1):
    """One horizontal bar split into segments toward a target. segments = [(label, value, tone)]."""
    left, right, y, bh = 24, W - 24, 56, 34
    scale = (right - left) / target
    x = left
    out = []
    tones = {"accent": "var(--accent)", "mid": "var(--accent-soft)", "gap": "none"}
    for i, (lab, v, tone) in enumerate(segments):
        w = v * scale
        if tone == "gap":
            out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bh}" fill="var(--paper)" '
                       f'stroke="var(--muted)" stroke-dasharray="4 4"/>')
        else:
            out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bh}" fill="{tones[tone]}"/>')
        anchor_x = x + 8
        out.append(f'<text x="{anchor_x:.1f}" y="{y - 12}" fill="var(--ink)" font-weight="600">{fmt(v, dec)}{unit}</text>'
                   f'<text x="{anchor_x:.1f}" y="{y + bh + 22}" fill="var(--muted)">{escape(lab)}</text>')
        x += w
    out.append(f'<line x1="{right}" x2="{right}" y1="{y - 26}" y2="{y + bh + 8}" stroke="var(--ink)" stroke-width="1.5"/>'
               f'<text x="{right}" y="{y - 32}" text-anchor="end" fill="var(--ink)" font-weight="600">{target_label} {fmt(target)}{unit}</text>')
    return _svg(h, label, "".join(out))
