import streamlit as st
import folium
from streamlit_folium import st_folium


# =========================================================
# SAYFA AYARLARI
# =========================================================

st.set_page_config(
    page_title="Amsterdam Gezi Planı",
    page_icon="🇳🇱",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    color: #1f4e79;
    font-size: 38px;
    font-weight: 700;
    margin-top: 0px;
    margin-bottom: 2px;
}

.date-title {
    text-align: center;
    color: #777;
    font-size: 14px;
    margin-bottom: 25px;
}


/* ANA SAYFADAKİ GÜN KARTLARI */

.day-card-button button {
    min-height: 125px !important;
    height: auto !important;
    width: 100% !important;

    background-color: #f5f8fc !important;

    border: 1px solid #dce5ef !important;
    border-radius: 14px !important;

    color: #555 !important;

    text-align: left !important;

    padding: 18px 25px !important;

    font-size: 14px !important;

    white-space: pre-line !important;

    box-shadow: none !important;
}


/* KART ÜZERİNE GELİNCE */

.day-card-button button:hover {
    background-color: #eef4fa !important;
    border: 2px solid #1f4e79 !important;
    color: #1f4e79 !important;
}


/* KART YAZILARI */

.day-card-button button p {
    white-space: pre-line !important;
    text-align: left !important;
}


/* DETAY SAYFASI */

h1 {
    color: #1f4e79;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HARİTA NUMARALI İKON
# =========================================================

def num_icon(number, color="#1f4e79"):

    return folium.DivIcon(
        html=f"""
        <div style="
            background:{color};
            color:white;
            border-radius:50%;
            width:34px;
            height:34px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:17px;
            font-weight:bold;
            border:3px solid white;
            box-shadow:0 2px 6px rgba(0,0,0,0.35);
        ">
            {number}
        </div>
        """
    )


# =========================================================
# GÖREV İKONU
# =========================================================

def task_icon(checked):

    if checked:

        return folium.DivIcon(
            html="""
            <div style="
                background:#28a745;
                color:white;
                border-radius:50%;
                width:32px;
                height:32px;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:18px;
                font-weight:bold;
                border:3px solid white;
                box-shadow:0 2px 6px rgba(0,0,0,0.35);
            ">
                ✓
            </div>
            """
        )

    return folium.DivIcon(
        html="""
        <div style="
            background:#ffc107;
            color:#222;
            border-radius:50%;
            width:32px;
            height:32px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:18px;
            font-weight:bold;
            border:3px solid white;
            box-shadow:0 2px 6px rgba(0,0,0,0.35);
        ">
            ★
        </div>
        """
    )


# =========================================================
# ROTA HARİTASI
# =========================================================

def create_route_map(route_points, center, zoom=13):

    m = folium.Map(
        location=center,
        zoom_start=zoom,
        tiles="OpenStreetMap"
    )

    # Rota koordinatları
    # tuple yapısı:
    # (numara, isim, enlem, boylam)

    coords = [
        (point[2], point[3])
        for point in route_points
    ]

    # Rota çizgisi
    folium.PolyLine(
        locations=coords,
        color="#1f4e79",
        weight=5,
        opacity=0.8
    ).add_to(m)

    # Numaralı duraklar
    for number, name, lat, lon in route_points:

        folium.Marker(
            location=[lat, lon],
            tooltip=name,
            popup=name,
            icon=num_icon(number)
        ).add_to(m)

    return m


# =========================================================
# KOORDİNATLAR
# =========================================================


# =========================================================
# 1. GÜN — 28 EYLÜL
# =========================================================

izmir = (
    38.4237,
    27.1428
)

dusseldorf_havalimani = (
    51.2895,
    6.7668
)

worringer = (
    51.2217,
    6.7948
)

amsterdam_sloterdijk = (
    52.3887,
    4.8377
)

hotel = (
    52.3788,
    4.8540
)

dam = (
    52.3731,
    4.8926
)


# ---------------------------------------------------------
# 1. GÜN GÖREVLERİ
# ---------------------------------------------------------

abraxas = (
    52.37206,
    4.89117
)

urban_outfitters = (
    52.371695,
    4.892120
)

snipes = (
    52.3709,
    4.8918
)

lego = (
    52.37084,
    4.89187
)

rubber_duck = (
    52.370414,
    4.892262
)

stroopwafel_1 = (
    52.3742333,
    4.8930022
)


day1_route = [

    (
        1,
        "İzmir",
        izmir[0],
        izmir[1]
    ),

    (
        2,
        "Düsseldorf Havalimanı",
        dusseldorf_havalimani[0],
        dusseldorf_havalimani[1]
    ),

    (
        3,
        "Worringer Strasse 140",
        worringer[0],
        worringer[1]
    ),

    (
        4,
        "Amsterdam Sloterdijk",
        amsterdam_sloterdijk[0],
        amsterdam_sloterdijk[1]
    ),

    (
        5,
        "Triple G Hotels",
        hotel[0],
        hotel[1]
    ),

    (
        6,
        "Dam Meydanı",
        dam[0],
        dam[1]
    ),

    (
        7,
        "Otele Dönüş - Triple G Hotels",
        hotel[0],
        hotel[1]
    )
]


day1_tasks = {

    "Abraxas": abraxas,

    "Urban Outfitters": urban_outfitters,

    "SNIPES": snipes,

    "LEGO Winkel Amsterdam": lego,

    "The Rubber Duck Store": rubber_duck,

    "Stroopwafel #1": stroopwafel_1
}


# =========================================================
# 2. GÜN — 29 EYLÜL
# =========================================================


cookies_lounge = (
    52.3799,
    4.8883
)

manneken_pis = (
    52.375789,
    4.896147
)

tonys = (
    52.37552,
    4.89687
)

sexmuseum = (
    52.37658,
    4.89728
)

basiliek = (
    52.37654,
    4.90083
)

red_light_secrets = (
    52.37365,
    4.89898
)

dam_day2 = (
    52.3731,
    4.8926
)

boat_dock = (52.378360, 4.897670)

green_house = (
    52.371494,
    4.895737
)

grimburgwal = (
    52.3693,
    4.8946
)


day2_route = [

    (
        1,
        "Triple G Hotels - Sabah Çıkış",
        hotel[0],
        hotel[1]
    ),

    (
        2,
        "Cookies Lounge",
        cookies_lounge[0],
        cookies_lounge[1]
    ),

    (
        3,
        "Manneken Pis Damrak",
        manneken_pis[0],
        manneken_pis[1]
    ),

    (
        4,
        "Tony's Chocolonely Super Store",
        tonys[0],
        tonys[1]
    ),

    (
        5,
        "Sexmuseum Amsterdam",
        sexmuseum[0],
        sexmuseum[1]
    ),

    (
        6,
        "Basiliek van de HH Nicolaas",
        basiliek[0],
        basiliek[1]
    ),

    (
        7,
        "Museum of Prostitution - Red Light Secrets",
        red_light_secrets[0],
        red_light_secrets[1]
    ),

    (
        8,
        "De Dam",
        dam_day2[0],
        dam_day2[1]
    ),

    (
        9,
        "Amsterdam Boat Experience's Dock",
        boat_dock[0],
        boat_dock[1]
    ),

    (
        10,
        "Green House Centrum",
        green_house[0],
        green_house[1]
    ),

    (
        11,
        "Grimburgwal Canal View",
        grimburgwal[0],
        grimburgwal[1]
    ),

    (
        12,
        "Triple G Hotels - Otele Dönüş",
        hotel[0],
        hotel[1]
    )
]


# =========================================================
# SESSION STATE
# =========================================================

if "sayfa" not in st.session_state:

    st.session_state.sayfa = "Ana Sayfa"


if "day1_tasks" not in st.session_state:

    st.session_state.day1_tasks = {
        gorev: False
        for gorev in day1_tasks
    }


# =========================================================
# ANA SAYFA
# =========================================================

if st.session_state.sayfa == "Ana Sayfa":


    # -----------------------------------------------------
    # BAŞLIK
    # -----------------------------------------------------

    st.markdown(
        '<div class="main-title">'
        '🇳🇱 AMSTERDAM GEZİ PLANI'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="date-title">'
        '28 Eylül - 1 Ekim'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # 1. GÜN KARTI
    # =====================================================

    st.markdown(
        '<div class="day-card-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "📅 28 Eylül — 1. Gün\n\n"
        "✈️ İzmir → Düsseldorf → Amsterdam\n\n"
        "Otele yerleşme • Dam Meydanı • Akşam gezisi",
        key="day1_card",
        use_container_width=True
    ):

        st.session_state.sayfa = "1. Gün"

        st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # 2. GÜN KARTI
    # =====================================================

    st.markdown(
        '<div class="day-card-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "📅 29 Eylül — 2. Gün\n\n"
        "🚶 Amsterdam merkez rotası • 🛥️ Tekne turu\n\n"
        "Cookies Lounge • Damrak • Red Light Secrets • "
        "Tekne • Green House • Grimburgwal",
        key="day2_card",
        use_container_width=True
    ):

        st.session_state.sayfa = "2. Gün"

        st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 1. GÜN DETAY
# =========================================================

elif st.session_state.sayfa == "1. Gün":


    # -----------------------------------------------------
    # GERİ
    # -----------------------------------------------------

    if st.button(
        "← ANA SAYFAYA DÖN",
        key="back_day1"
    ):

        st.session_state.sayfa = "Ana Sayfa"

        st.rerun()


    st.title("📅 28 Eylül — 1. Gün")

    st.markdown("---")


    # -----------------------------------------------------
    # 1
    # -----------------------------------------------------

    st.subheader(
        "1) ✈️ KALKIŞ UÇUŞU"
    )

    st.write(
        "✈️ İzmir → Düsseldorf"
    )

    st.write(
        "🕕 06:10 — Kalkış"
    )


    # -----------------------------------------------------
    # 2
    # -----------------------------------------------------

    st.subheader(
        "2) 🛬 İNİŞ"
    )

    st.write(
        "🛬 Düsseldorf Havalimanı"
    )

    st.write(
        "🕣 08:30 — Varış"
    )


    # -----------------------------------------------------
    # 3
    # -----------------------------------------------------

    st.subheader(
        "3) 🚌 FLIXBUS BİNİŞ"
    )

    st.write(
        "📍 Worringer Strasse 140"
    )

    st.write(
        "🕥 10:30 — Kalkış"
    )


    # -----------------------------------------------------
    # 4
    # -----------------------------------------------------

    st.subheader(
        "4) 🇳🇱 AMSTERDAM'A VARIŞ"
    )

    st.write(
        "📍 Amsterdam Sloterdijk"
    )

    st.write(
        "🕝 14:30 — Tahmini varış"
    )


    # -----------------------------------------------------
    # 5
    # -----------------------------------------------------

    st.subheader(
        "5) 🏠 OTELE VARIŞ"
    )

    st.write(
        "🏠 Triple G Hotels"
    )

    st.write(
        "📍 Willem de Zwijgerlaan 350"
    )

    st.write(
        "📍 1055 RD Amsterdam"
    )

    st.write(
        "🕒 15:00 — Tahmini varış"
    )

    st.write(
        "😴 15:00–17:00 — Dinlenme / hazırlanma"
    )


    # -----------------------------------------------------
    # 6
    # -----------------------------------------------------

    st.subheader(
        "6) 🌆 AKŞAM GEZİSİ / YEMEK"
    )

    st.write(
        "🚶 17:00 — Otelden çıkış"
    )

    st.write(
        "🕠 ≈17:30 — Dam Meydanı"
    )

    st.write(
        "🍽️ 18:00 civarı — Akşam yemeği"
    )


    # -----------------------------------------------------
    # GÖREVLER
    # -----------------------------------------------------

    st.markdown(
        "### 🎯 Gidilecek Yerler"
    )


    for gorev in day1_tasks:

        checked = st.checkbox(
            gorev,
            value=st.session_state.day1_tasks[gorev],
            key=f"day1_task_{gorev}"
        )

        st.session_state.day1_tasks[gorev] = checked


    # -----------------------------------------------------
    # 7
    # -----------------------------------------------------

    st.subheader(
        "7) 🏠 OTELE DÖNÜŞ"
    )

    st.write(
        "🏠 Triple G Hotels"
    )

    st.write(
        "🕙 22:00 — Otele dönüş"
    )


    # -----------------------------------------------------
    # HARİTA
    # -----------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🗺️ 1. Gün Rotası"
    )


    m1 = create_route_map(
        day1_route,
        center=(52.35, 4.87),
        zoom=10
    )


    # Görev ikonları

    for gorev, coords in day1_tasks.items():

        checked = st.session_state.day1_tasks[gorev]

        folium.Marker(
            location=coords,
            tooltip=gorev,
            popup=gorev,
            icon=task_icon(checked)
        ).add_to(m1)


    st_folium(
        m1,
        width=None,
        height=550,
        key="map_day1"
    )


# =========================================================
# 2. GÜN DETAY — 29 EYLÜL
# =========================================================

elif st.session_state.sayfa == "2. Gün":


    # -----------------------------------------------------
    # GERİ
    # -----------------------------------------------------

    if st.button(
        "← ANA SAYFAYA DÖN",
        key="back_day2"
    ):

        st.session_state.sayfa = "Ana Sayfa"

        st.rerun()


    st.title(
        "📅 29 Eylül — 2. Gün"
    )

    st.markdown("---")


    # -----------------------------------------------------
    # 1
    # -----------------------------------------------------

    st.subheader(
        "1) 🏠 OTELE ÇIKIŞ"
    )

    st.write(
        "🏠 Triple G Hotels"
    )

    st.write(
        "🕙 10:00 — Otelden çıkış"
    )


    # -----------------------------------------------------
    # 2
    # -----------------------------------------------------

    st.subheader(
        "2) 🌿 COOKIES LOUNGE"
    )

    st.write(
        "🕥 10:40–11:30 — Cookies Lounge"
    )

    st.write(
        "☕ Rahat bir başlangıç / oturma"
    )


    # -----------------------------------------------------
    # 3
    # -----------------------------------------------------

    st.subheader(
        "3) 🍟 MANNEKEN PIS DAMRAK"
    )

    st.write(
        "🚶 11:30–11:45 — Yürüyüş"
    )

    st.write(
        "🕦 11:45–12:15 — Manneken Pis"
    )


    # -----------------------------------------------------
    # 4
    # -----------------------------------------------------

    st.subheader(
        "4) 🍫 TONY'S CHOCOLONELY"
    )

    st.write(
        "🚶 12:15–12:25 — Yürüyüş"
    )

    st.write(
        "🕧 12:25–13:10 — Tony's Chocolonely Super Store"
    )


    # -----------------------------------------------------
    # 5
    # -----------------------------------------------------

    st.subheader(
        "5) 🎉 SEXMUSEUM AMSTERDAM"
    )

    st.write(
        "🚶 13:10–13:20 — Yürüyüş"
    )

    st.write(
        "🕐 13:20–14:15 — Sexmuseum Amsterdam"
    )


    # -----------------------------------------------------
    # 6
    # -----------------------------------------------------

    st.subheader(
        "6) ⛪ BASILIEK VAN DE HH NICOLAAS"
    )

    st.write(
        "🚶 14:15–14:25 — Yürüyüş"
    )

    st.write(
        "🕝 14:25–14:55 — Basiliek van de HH Nicolaas"
    )


    # -----------------------------------------------------
    # 7
    # -----------------------------------------------------

    st.subheader(
        "7) 🎉 RED LIGHT SECRETS"
    )

    st.write(
        "🚶 14:55–15:05 — Yürüyüş"
    )

    st.write(
        "🕒 15:05–15:50 — Museum of Prostitution – "
        "Red Light Secrets"
    )


    # -----------------------------------------------------
    # 8
    # -----------------------------------------------------

    st.subheader(
        "8) 🎉 DE DAM"
    )

    st.write(
        "🕓 15:50–16:40 — De Dam"
    )

    st.write(
        "📸 Gündüz tekrar gezme / fotoğraf"
    )


    # -----------------------------------------------------
    # 9
    # -----------------------------------------------------

    st.subheader(
        "9) 🍽️ YEMEK MOLASI"
    )

    st.write(
        "🕟 16:40–17:10"
    )

    st.write(
        "🍽️ Yemek molası"
    )


    # -----------------------------------------------------
    # 10
    # -----------------------------------------------------

    st.subheader(
        "10) 🛥️ TEKNE TURU"
    )

    st.write(
        "🚶 17:10–17:30 — Tekne iskelesine geçiş"
    )

    st.write(
        "📍 17:30 — Amsterdam Boat Experience's Dock"
    )

    st.write(
        "🕠 17:45–18:45 — 1 saatlik tekne turu"
    )


    # -----------------------------------------------------
    # 11
    # -----------------------------------------------------

    st.subheader(
        "11) 🌿 GREEN HOUSE CENTRUM"
    )

    st.write(
        "🚶 18:45–19:15 — Senin çizdiğin güzergâhtan yürüyüş"
    )

    st.write(
        "🕖 19:15–20:00 — Green House Centrum"
    )

    st.write(
        "🌿 Biraz oturma / oyalanma"
    )


    # -----------------------------------------------------
    # 12
    # -----------------------------------------------------

    st.subheader(
        "12) 📸 GRIMBURGWAL CANAL VIEW"
    )

    st.write(
        "🍽️ 20:00–20:30 — Yemek molası"
    )

    st.write(
        "📸 ≈20:30–20:50 — Grimburgwal Canal View"
    )


    # -----------------------------------------------------
    # 13
    # -----------------------------------------------------

    st.subheader(
        "13) 🏠 OTELE DÖNÜŞ"
    )

    st.write(
        "🏠 ≈21:45 — Triple G Hotels'e tahmini varış"
    )


    # -----------------------------------------------------
    # HARİTA
    # -----------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🗺️ 29 Eylül Rotası"
    )


    m2 = create_route_map(
        day2_route,
        center=(52.375, 4.895),
        zoom=13
    )


    st_folium(
        m2,
        width=None,
        height=600,
        key="map_day2"
    )