"""NTU-MARA Database & Programming — Final Project Gallery."""

import streamlit as st

from projects import PROJECTS

st.set_page_config(
    page_title="Final Project Gallery",
    page_icon="📊",
    layout="wide",
)

CATEGORY_COLOURS = {
    "Finance & Investment": "blue",
    "Insurance": "violet",
    "Risk & Compliance": "red",
    "Environment & Climate": "green",
    "Property & Public Data": "orange",
    "Customer Analytics": "primary",
}
COLUMNS = 3

st.markdown(
    """
    <style>
      .block-container { padding-top: 2.5rem; max-width: 1200px; }
      .proj-num { font-size: 0.8rem; letter-spacing: 0.08em; opacity: 0.6; margin-bottom: -0.6rem; }
      .proj-title { font-size: 1.2rem; font-weight: 700; line-height: 1.3; min-height: 3.2em; margin: 0.4rem 0 0.2rem; }
      .proj-desc { min-height: 4.8em; opacity: 0.85; }
      .proj-team { font-size: 0.85rem; opacity: 0.7; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
st.title("Final Project Gallery")
st.caption("NTU-MARA · Database & Programming · Group final projects built with Python, SQL and Streamlit")

live = [p for p in PROJECTS if p["app_url"].strip()]
m1, m2, m3 = st.columns(3)
m1.metric("Projects", len(PROJECTS))
m2.metric("Live dashboards", len(live))
m3.metric("Themes", len({p["category"] for p in PROJECTS}))

st.divider()

# ---------- Filters ----------
f1, f2 = st.columns([3, 1], vertical_alignment="bottom")
query = f1.text_input("Search", placeholder="Search by title, description or team…", label_visibility="collapsed")
live_only = f2.toggle("Live only", value=False)

categories = sorted({p["category"] for p in PROJECTS})
picked = st.pills("Theme", categories, selection_mode="multi", label_visibility="collapsed")


def matches(p: dict) -> bool:
    if live_only and not p["app_url"].strip():
        return False
    if picked and p["category"] not in picked:
        return False
    if query:
        haystack = " ".join(
            [p["title"], p["description"], p.get("team", ""), " ".join(p.get("members", []))]
        ).lower()
        return query.lower() in haystack
    return True


# Keep the original project numbers even when filtered.
shown = [(i, p) for i, p in enumerate(PROJECTS, start=1) if matches(p)]

if not shown:
    st.info("No projects match those filters.")
    st.stop()


# ---------- Cards ----------
def render_card(num: int, p: dict) -> None:
    with st.container(border=True):
        st.markdown(f'<div class="proj-num">PROJECT {num:02d}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="proj-title">{p["title"]}</div>', unsafe_allow_html=True)

        colour = CATEGORY_COLOURS.get(p["category"], "gray")
        status = ":green-badge[● Live]" if p["app_url"].strip() else ":gray-badge[Coming soon]"
        st.markdown(f":{colour}-badge[{p['category']}] &nbsp; {status}")

        st.markdown(f'<div class="proj-desc">{p["description"]}</div>', unsafe_allow_html=True)

        team_bits = [b for b in [p.get("team", ""), ", ".join(p.get("members", []))] if b]
        if team_bits:
            st.markdown(f'<div class="proj-team">👥 {" — ".join(team_bits)}</div>', unsafe_allow_html=True)

        b1, b2 = st.columns(2)
        if p["app_url"].strip():
            b1.link_button("Open dashboard ↗", p["app_url"], type="primary", width="stretch")
        else:
            b1.button("Open dashboard", disabled=True, width="stretch", key=f"na-{num}")
        if p.get("repo_url", "").strip():
            b2.link_button("Source code", p["repo_url"], width="stretch")


for row_start in range(0, len(shown), COLUMNS):
    cols = st.columns(COLUMNS)
    for col, (num, p) in zip(cols, shown[row_start : row_start + COLUMNS]):
        with col:
            render_card(num, p)

st.divider()
st.caption(
    "Dashboards are hosted on Streamlit Community Cloud. An app that hasn't been used for a while "
    "goes to sleep — click “Yes, get this app back up” and give it a minute to wake."
)
