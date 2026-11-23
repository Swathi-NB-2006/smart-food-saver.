import streamlit as st
from datetime import datetime, timedelta
import uuid

# ─────────────────────────────────────────────
# PAGE CONFIG  (must be FIRST streamlit call)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Food Saver",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS  – green & white modern theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ---- Google Font ---- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ---- App background ---- */
.stApp { background: #f0faf4; }

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a7a4a 0%, #145c38 100%);
}
[data-testid="stSidebar"] * { color: #ffffff !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 15px; font-weight: 500; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.15);
    border-radius: 8px;
    padding: 4px 8px;
}

/* ---- Metric cards ---- */
[data-testid="metric-container"] {
    background: #ffffff;
    border: 1px solid #c8ecd7;
    border-left: 5px solid #22a05a;
    border-radius: 12px;
    padding: 16px 20px;
    box-shadow: 0 2px 8px rgba(34,160,90,0.08);
}
[data-testid="metric-container"] [data-testid="stMetricLabel"] { color: #2d6a4f; font-weight: 600; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: #1a7a4a; font-size: 2rem; font-weight: 800; }

/* ---- Buttons ---- */
.stButton > button {
    background: linear-gradient(135deg, #22a05a 0%, #1a7a4a 100%);
    color: #ffffff;
    border: none;
    border-radius: 10px;
    padding: 10px 24px;
    font-weight: 600;
    font-size: 15px;
    transition: transform .15s, box-shadow .15s;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(34,160,90,0.35);
    color: #ffffff;
}

/* ---- Form inputs ---- */
.stTextInput input, .stNumberInput input, .stSelectbox select,
.stDateInput input, .stTimeInput input {
    border: 1.5px solid #b7dfc9;
    border-radius: 8px;
    background: #ffffff;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #22a05a;
    box-shadow: 0 0 0 3px rgba(34,160,90,0.15);
}

/* ---- Food cards ---- */
.food-card {
    background: #ffffff;
    border-radius: 16px;
    border: 1px solid #c8ecd7;
    box-shadow: 0 4px 16px rgba(34,160,90,0.08);
    padding: 20px;
    margin-bottom: 16px;
    transition: transform .2s;
}
.food-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(34,160,90,0.14); }
.food-card h3 { margin: 0 0 8px; color: #1a7a4a; font-size: 20px; }
.food-card p  { margin: 4px 0; color: #4a7a5e; font-size: 14px; }
.badge-available {
    display: inline-block;
    background: #d4f1e4;
    color: #1a7a4a;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 10px;
}
.badge-collected {
    display: inline-block;
    background: #fff3cd;
    color: #856404;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 10px;
}
.hero-banner {
    background: linear-gradient(135deg, #22a05a 0%, #1a7a4a 100%);
    color: white;
    border-radius: 20px;
    padding: 36px 40px;
    margin-bottom: 28px;
    text-align: center;
}
.hero-banner h1 { font-size: 2.4rem; font-weight: 800; margin: 0; }
.hero-banner p  { font-size: 1.1rem; margin: 8px 0 0; opacity: 0.9; }

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a7a4a;
    border-left: 5px solid #22a05a;
    padding-left: 12px;
    margin: 24px 0 16px;
}
.info-box {
    background: #d4f1e4;
    border-radius: 10px;
    padding: 14px 18px;
    color: #1a7a4a;
    font-size: 14px;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SESSION STATE  –  initialise once
# ─────────────────────────────────────────────
def init_state():
    """Create all session-state variables on first run."""
    if "food_items" not in st.session_state:
        now = datetime.now()
        st.session_state.food_items = [
            {
                "id": str(uuid.uuid4()),
                "name": "Vegetable Biryani",
                "quantity": 15,
                "unit": "servings",
                "location": "Main Canteen – Counter 2",
                "pickup_time": (now + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M"),
                "added_by": "Canteen Staff",
                "added_at": now.strftime("%Y-%m-%d %H:%M"),
                "status": "available",
                "emoji": "🍛",
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Bread Rolls",
                "quantity": 30,
                "unit": "pieces",
                "location": "Block B Canteen",
                "pickup_time": (now + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"),
                "added_by": "Canteen Staff",
                "added_at": now.strftime("%Y-%m-%d %H:%M"),
                "status": "available",
                "emoji": "🍞",
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Dal Tadka + Rice",
                "quantity": 20,
                "unit": "servings",
                "location": "Main Canteen – Counter 1",
                "pickup_time": (now + timedelta(hours=3)).strftime("%Y-%m-%d %H:%M"),
                "added_by": "Canteen Staff",
                "added_at": now.strftime("%Y-%m-%d %H:%M"),
                "status": "available",
                "emoji": "🥘",
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Fresh Fruit Salad",
                "quantity": 10,
                "unit": "bowls",
                "location": "Juice Corner – Ground Floor",
                "pickup_time": (now + timedelta(hours=1, minutes=30)).strftime("%Y-%m-%d %H:%M"),
                "added_by": "Canteen Staff",
                "added_at": now.strftime("%Y-%m-%d %H:%M"),
                "status": "available",
                "emoji": "🍓",
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Samosas",
                "quantity": 25,
                "unit": "pieces",
                "location": "Snack Stall – Block A",
                "pickup_time": (now + timedelta(minutes=45)).strftime("%Y-%m-%d %H:%M"),
                "added_by": "Canteen Staff",
                "added_at": (now - timedelta(minutes=20)).strftime("%Y-%m-%d %H:%M"),
                "status": "collected",
                "emoji": "🥟",
            },
        ]
    if "notification" not in st.session_state:
        st.session_state.notification = None


init_state()


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
EMOJI_MAP = {
    "rice": "🍚", "biryani": "🍛", "dal": "🥘", "curry": "🍲",
    "bread": "🍞", "roti": "🫓", "chapati": "🫓", "paratha": "🫓",
    "fruit": "🍓", "salad": "🥗", "juice": "🧃", "milk": "🥛",
    "sandwich": "🥪", "burger": "🍔", "pizza": "🍕", "noodle": "🍜",
    "pasta": "🍝", "soup": "🍜", "samosa": "🥟", "idli": "🫓",
    "dosa": "🫓", "upma": "🥣", "poha": "🥣", "cake": "🎂",
    "sweet": "🍮", "kheer": "🍮", "halwa": "🍮", "snack": "🍿",
    "biscuit": "🍪", "egg": "🥚", "paneer": "🧀",
}

def pick_emoji(name: str) -> str:
    name_lower = name.lower()
    for key, emoji in EMOJI_MAP.items():
        if key in name_lower:
            return emoji
    return "🍽️"


def get_stats():
    items = st.session_state.food_items
    total_added    = sum(i["quantity"] for i in items)
    total_collected = sum(i["quantity"] for i in items if i["status"] == "collected")
    total_available = sum(i["quantity"] for i in items if i["status"] == "available")
    return total_added, total_collected, total_available


def mark_collected(item_id: str):
    for item in st.session_state.food_items:
        if item["id"] == item_id:
            item["status"] = "collected"
            st.session_state.notification = f"✅ '{item['name']}' has been marked as collected!"
            break


# ─────────────────────────────────────────────
# SIDEBAR  NAVIGATION
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🥗 Smart Food Saver")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["🏠  Dashboard", "➕  Add Surplus Food", "🍽️  Available Food", "ℹ️  About"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    total_added, total_collected, total_available = get_stats()
    st.markdown(f"**📦 Total Items Added:** {len(st.session_state.food_items)}")
    st.markdown(f"**✅ Items Collected:** {sum(1 for i in st.session_state.food_items if i['status']=='collected')}")
    st.markdown(f"**🟢 Items Available:** {sum(1 for i in st.session_state.food_items if i['status']=='available')}")
    st.markdown("---")
    st.markdown("<small style='opacity:0.7'>Helping colleges fight food waste 💚</small>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# NOTIFICATION BANNER
# ─────────────────────────────────────────────
if st.session_state.notification:
    st.success(st.session_state.notification)
    st.session_state.notification = None


# ══════════════════════════════════════════════
# PAGE 1 – DASHBOARD
# ══════════════════════════════════════════════
if page == "🏠  Dashboard":

    st.markdown("""
    <div class="hero-banner">
        <h1>🥗 Smart Food Saver</h1>
        <p>Connecting college canteens with students to reduce food waste</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row ──
    st.markdown('<div class="section-title">📊 Live Dashboard</div>', unsafe_allow_html=True)
    total_added, total_collected, total_available = get_stats()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🍱 Total Surplus Added", f"{total_added}", help="Total food quantity added by canteens")
    with col2:
        st.metric("✅ Food Collected", f"{total_collected}", help="Quantity collected by students/volunteers")
    with col3:
        st.metric("🟢 Currently Available", f"{total_available}", help="Still available for collection")
    with col4:
        waste_saved_kg = round(total_collected * 0.25, 1)
        st.metric("🌍 Waste Saved (est.)", f"{waste_saved_kg} kg", help="Estimated food saved from landfill")

    # ── Progress bar ──
    if total_added > 0:
        pct = total_collected / total_added
        st.markdown('<div class="section-title">📈 Collection Progress</div>', unsafe_allow_html=True)
        st.progress(pct, text=f"{int(pct*100)}% of surplus food collected today")

    # ── Recent activity ──
    st.markdown('<div class="section-title">🕐 Recent Food Entries</div>', unsafe_allow_html=True)
    recent = sorted(st.session_state.food_items, key=lambda x: x["added_at"], reverse=True)[:5]

    for item in recent:
        badge = "badge-available" if item["status"] == "available" else "badge-collected"
        badge_text = "🟢 Available" if item["status"] == "available" else "✅ Collected"
        st.markdown(f"""
        <div class="food-card">
            <span class="{badge}">{badge_text}</span>
            <h3>{item['emoji']} {item['name']}</h3>
            <p>📦 Quantity: <b>{item['quantity']} {item['unit']}</b></p>
            <p>📍 Location: {item['location']}</p>
            <p>⏰ Pickup before: {item['pickup_time']}</p>
        </div>
        """, unsafe_allow_html=True)

    # ── Quick action ──
    st.markdown('<div class="section-title">⚡ Quick Actions</div>', unsafe_allow_html=True)
    qa1, qa2 = st.columns(2)
    with qa1:
        if st.button("➕ Add Surplus Food", use_container_width=True):
            st.info("👉 Use the **'Add Surplus Food'** option in the sidebar!")
    with qa2:
        if st.button("🍽️ View Available Food", use_container_width=True):
            st.info("👉 Use the **'Available Food'** option in the sidebar!")


# ══════════════════════════════════════════════
# PAGE 2 – ADD SURPLUS FOOD
# ══════════════════════════════════════════════
elif page == "➕  Add Surplus Food":

    st.markdown('<div class="section-title">➕ Add Surplus Food</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        📢 Canteen staff: Fill in the form below to list surplus food so students and volunteers can collect it quickly.
    </div>
    """, unsafe_allow_html=True)

    with st.form("add_food_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            food_name = st.text_input("🍽️ Food Name *", placeholder="e.g. Vegetable Biryani")
            quantity  = st.number_input("📦 Quantity *", min_value=1, max_value=500, value=10, step=1)
            unit      = st.selectbox("📏 Unit", ["servings", "pieces", "bowls", "plates", "kg", "litres", "packets"])

        with col2:
            location    = st.text_input("📍 Pickup Location *", placeholder="e.g. Main Canteen – Counter 1")
            pickup_date = st.date_input("📅 Last Pickup Date", value=datetime.now().date())
            pickup_time = st.time_input("⏰ Last Pickup Time", value=datetime.now().replace(minute=0, second=0).time())

        notes       = st.text_area("📝 Additional Notes (optional)", placeholder="Any allergies, packaging info, etc.")
        staff_name  = st.text_input("👤 Your Name / Staff ID", placeholder="e.g. Ravi (Canteen Head)")

        submitted = st.form_submit_button("🚀 Add Food Entry", use_container_width=True)

    if submitted:
        # ── Validation ──
        errors = []
        if not food_name.strip():
            errors.append("Food name is required.")
        if not location.strip():
            errors.append("Pickup location is required.")

        if errors:
            for e in errors:
                st.error(f"❌ {e}")
        else:
            pickup_dt = datetime.combine(pickup_date, pickup_time).strftime("%Y-%m-%d %H:%M")
            new_item = {
                "id":          str(uuid.uuid4()),
                "name":        food_name.strip(),
                "quantity":    quantity,
                "unit":        unit,
                "location":    location.strip(),
                "pickup_time": pickup_dt,
                "added_by":    staff_name.strip() or "Canteen Staff",
                "added_at":    datetime.now().strftime("%Y-%m-%d %H:%M"),
                "status":      "available",
                "notes":       notes.strip(),
                "emoji":       pick_emoji(food_name),
            }
            st.session_state.food_items.append(new_item)
            st.session_state.notification = f"🎉 '{food_name}' added successfully! Students can now see it."
            st.rerun()

    # ── Preview of recent additions ──
    st.markdown('<div class="section-title">📋 Recently Added (last 3)</div>', unsafe_allow_html=True)
    recent3 = [i for i in reversed(st.session_state.food_items)][:3]
    for item in recent3:
        badge = "badge-available" if item["status"] == "available" else "badge-collected"
        badge_text = "🟢 Available" if item["status"] == "available" else "✅ Collected"
        st.markdown(f"""
        <div class="food-card">
            <span class="{badge}">{badge_text}</span>
            <h3>{item['emoji']} {item['name']}</h3>
            <p>📦 {item['quantity']} {item['unit']} &nbsp;|&nbsp; 📍 {item['location']}</p>
            <p>⏰ Pickup before: {item['pickup_time']}</p>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PAGE 3 – AVAILABLE FOOD (student view)
# ══════════════════════════════════════════════
elif page == "🍽️  Available Food":

    st.markdown('<div class="section-title">🍽️ Available Surplus Food</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        🎓 Students & volunteers: Browse available food below and click <b>"Request / Collect"</b> to claim it.
        Please collect promptly before the pickup deadline!
    </div>
    """, unsafe_allow_html=True)

    # ── Filter bar ──
    search_term = st.text_input("🔍 Search food...", placeholder="Type a food name or location")

    show_all = st.checkbox("Show collected items too", value=False)

    items = st.session_state.food_items
    if not show_all:
        items = [i for i in items if i["status"] == "available"]
    if search_term:
        items = [i for i in items if
                 search_term.lower() in i["name"].lower() or
                 search_term.lower() in i["location"].lower()]

    if not items:
        st.warning("😕 No food items match your search. Check back soon or try a different search term!")
    else:
        # 2-column card grid
        cols = st.columns(2)
        for idx, item in enumerate(items):
            with cols[idx % 2]:
                badge      = "badge-available" if item["status"] == "available" else "badge-collected"
                badge_text = "🟢 Available" if item["status"] == "available" else "✅ Collected"
                notes_html = f"<p>📝 {item.get('notes','')}</p>" if item.get("notes") else ""
                st.markdown(f"""
                <div class="food-card">
                    <span class="{badge}">{badge_text}</span>
                    <h3>{item['emoji']} {item['name']}</h3>
                    <p>📦 Quantity: <b>{item['quantity']} {item['unit']}</b></p>
                    <p>📍 Location: {item['location']}</p>
                    <p>⏰ Pickup before: {item['pickup_time']}</p>
                    <p>👤 Added by: {item['added_by']}</p>
                    {notes_html}
                </div>
                """, unsafe_allow_html=True)

                if item["status"] == "available":
                    if st.button(f"🙋 Request / Collect – {item['name']}", key=f"collect_{item['id']}",
                                 use_container_width=True):
                        mark_collected(item["id"])
                        st.rerun()
                else:
                    st.markdown(
                        "<p style='color:#856404;font-weight:600;text-align:center;'>✅ Already Collected</p>",
                        unsafe_allow_html=True,
                    )

    # ── Stats summary ──
    st.markdown("---")
    total_added, total_collected, total_available = get_stats()
    s1, s2, s3 = st.columns(3)
    s1.metric("🟢 Available Now", total_available)
    s2.metric("✅ Collected", total_collected)
    s3.metric("📦 Total Added", total_added)


# ══════════════════════════════════════════════
# PAGE 4 – ABOUT
# ══════════════════════════════════════════════
elif page == "ℹ️  About":

    st.markdown("""
    <div class="hero-banner">
        <h1>ℹ️ About Smart Food Saver</h1>
        <p>A hackathon project to fight college canteen food waste</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 The Problem
        College canteens prepare food in bulk every day.
        Leftover surplus food often gets thrown away even though many students
        or volunteers could use it — simply because there is **no easy way to
        communicate** about it in real time.

        ### 💡 Our Solution
        **Smart Food Saver** is a lightweight web app that lets:
        - **Canteen staff** post surplus food in seconds.
        - **Students & volunteers** see what's available and claim it instantly.
        - Everyone track how much food (and CO₂) has been saved.
        """)
    with col2:
        st.markdown("""
        ### ✨ Key Features
        | Feature | Details |
        |---|---|
        | 📊 Live Dashboard | Real-time stats on surplus & collected food |
        | ➕ Add Food | Simple form for canteen staff |
        | 🍽️ Browse & Claim | Card view + one-click collection |
        | 🌍 Waste Tracker | Estimates of food waste prevented |
        | 💚 Green Design | Clean, mobile-friendly UI |

        ### 🛠️ Tech Stack
        | Layer | Tool |
        |---|---|
        | Language | Python 3.9+ |
        | Framework | Streamlit |
        | Storage | Session State (in-memory) |
        | Design | Custom CSS |
        """)

    st.markdown("""
    ### 🚀 How to Run
    ```bash
    # 1. Install dependencies
    pip install -r requirements.txt

    # 2. Run the app
    streamlit run app.py
    ```
    Then open **http://localhost:8501** in your browser.

    ### 👥 Built for
    This project was built as a hackathon entry to demonstrate how a simple
    digital tool can make a real-world impact on food waste reduction in colleges.
    """)

    st.success("💚 Together we can reduce food waste, one meal at a time!")
