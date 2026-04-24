import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="🚜 రైతు AI", layout="centered")

st.title("🚜 రైతు AI - పంట వ్యాధి సహాయ వ్యవస్థ")
st.write("👉 పంట స్థితిని ఎంచుకోండి | తెలుగు సలహాలు + ప్రో చిట్కాలు + ప్రభుత్వ పథకాలు")

# =========================
# DISEASE DATA
# =========================
disease_info = {

    "Healthy (ఆరోగ్యమైన పంట)": {
        "tips": [
            "మీ పంట ఆరోగ్యంగా ఉంది 👍",
            "ప్రతి 10 రోజులకు పరిశీలించండి",
            "ఉదయం నీటిపారుదల చేయండి",
            "⚡ అత్యవసరం: మార్పు కనిపిస్తే వెంటనే చర్యలు తీసుకోండి"
        ],
        "pro_tips": [
            "జీవామృతం వాడితే soil health మెరుగవుతుంది",
            "mixed cropping చేస్తే pests తగ్గుతాయి"
        ]
    },

    "Leaf Blight (ఆకు కాల్చు)": {
        "tips": [
            "ఆకులు కాలిపోతున్నాయి ⚠️",
            "ప్రభావిత ఆకులు తొలగించండి",
            "నత్రజని ఎరువు తగ్గించండి",
            "⚡ అత్యవసరం: ఫంగిసైడ్ స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "ఉదయం మాత్రమే నీరు పెట్టండి",
            "spacing పెంచండి",
            "Trichoderma వాడండి"
        ]
    },

    "Root Rot (వేరు కుళ్ళు)": {
        "tips": [
            "వేర్లు కుళ్లిపోతున్నాయి ⚠️",
            "నీరు తగ్గించండి",
            "⚡ అత్యవసరం: మొక్క తొలగించండి"
        ],
        "pro_tips": [
            "raised beds వాడండి",
            "drainage improve చేయండి"
        ]
    },

    "Powdery Mildew (పొడి మచ్చ)": {
        "tips": [
            "తెల్ల పొడి కనిపిస్తోంది ⚠️",
            "Neem oil వాడండి",
            "⚡ అత్యవసరం: పాలు+నీరు స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "weekly milk spray చేయండి",
            "sunlight పెంచండి"
        ]
    },

    "Rust (రస్ట్ వ్యాధి)": {
        "tips": [
            "ఆకులపై తుప్పు మచ్చలు ⚠️",
            "తేమ తగ్గించండి",
            "⚡ అత్యవసరం: Sulfur స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "crop rotation చేయండి",
            "resistant seeds వాడండి"
        ]
    },

    "Bacterial Spot (బ్యాక్టీరియా మచ్చ)": {
        "tips": [
            "ఆకులపై మచ్చలు ⚠️",
            "పరికరాలు శుభ్రం చేయండి",
            "⚡ అత్యవసరం: కాపర్ స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "seed treatment చేయండి",
            "overwatering నివారించండి"
        ]
    },

    "Wilt (వాడిపోవడం)": {
        "tips": [
            "మొక్క వాడిపోతోంది ⚠️",
            "నీరు సరిచూడండి",
            "⚡ అత్యవసరం: మొక్క తొలగించండి"
        ],
        "pro_tips": [
            "soil solarization చేయండి",
            "resistant seeds వాడండి"
        ]
    },

    "Leaf Spot (ఆకు మచ్చ)": {
        "tips": [
            "మచ్చలు కనిపిస్తున్నాయి ⚠️",
            "Neem oil వాడండి",
            "⚡ అత్యవసరం: ఆకులు తొలగించండి"
        ],
        "pro_tips": [
            "early detection చేయండి",
            "drip irrigation వాడండి"
        ]
    },

    "Downy Mildew (డౌనీ మిల్డ్యూ)": {
        "tips": [
            "ఫంగస్ పెరుగుతోంది ⚠️",
            "తేమ తగ్గించండి",
            "⚡ అత్యవసరం: స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "morning irrigation చేయండి",
            "air flow maintain చేయండి"
        ]
    },

    "Anthracnose (అంత్రాక్నోస్)": {
        "tips": [
            "నల్ల మచ్చలు ⚠️",
            "seed treatment చేయండి",
            "⚡ అత్యవసరం: ఫంగిసైడ్ వాడండి"
        ],
        "pro_tips": [
            "infected fruits తొలగించండి",
            "mulching వాడండి"
        ]
    },

    "Canker (క్యాంకర్)": {
        "tips": [
            "కొమ్మలపై గాయాలు ⚠️",
            "కత్తిరించండి",
            "⚡ అత్యవసరం: కాపర్ స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "clean tools వాడండి",
            "wounds seal చేయండి"
        ]
    },

    "Scab (స్కాబ్)": {
        "tips": [
            "గట్టిపడిన మచ్చలు ⚠️",
            "శుభ్రత పాటించండి",
            "⚡ అత్యవసరం: స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "fallen leaves తొలగించండి",
            "preventive spray చేయండి"
        ]
    },

    "Mosaic Virus (మోజాయిక్ వైరస్)": {
        "tips": [
            "డిజైన్ లాగా మచ్చలు ⚠️",
            "కీటక నియంత్రణ చేయండి",
            "⚡ అత్యవసరం: మొక్క తొలగించండి"
        ],
        "pro_tips": [
            "aphids control చేయండి",
            "resistant seeds వాడండి"
        ]
    },

    "Stem Rot (కాండం కుళ్ళు)": {
        "tips": [
            "కాండం కుళ్లిపోతోంది ⚠️",
            "నీరు తగ్గించండి",
            "⚡ అత్యవసరం: మొక్క తొలగించండి"
        ],
        "pro_tips": [
            "soil drainage మెరుగుపరచండి",
            "bio fungicides వాడండి"
        ]
    },

    "Fruit Rot (పండు కుళ్ళు)": {
        "tips": [
            "పండ్లు పాడవుతున్నాయి ⚠️",
            "పండ్లు నేల తాకనివ్వండి",
            "⚡ అత్యవసరం: పాడైన పండ్లు తొలగించండి"
        ],
        "pro_tips": [
            "mulching వాడండి",
            "harvesting జాగ్రత్తగా చేయండి"
        ]
    },

    "Blast (బ్లాస్ట్)": {
        "tips": [
            "కాలినట్టు కనిపిస్తుంది ⚠️",
            "నీరు నియంత్రించండి",
            "⚡ అత్యవసరం: స్ప్రే చేయండి"
        ],
        "pro_tips": [
            "balanced fertilizers వాడండి",
            "early detection చేయండి"
        ]
    }
}

# =========================
# GOVT SCHEMES
# =========================
insurance_schemes = {
    disease: [
        {
            "name": "ప్రధాన మంత్రి ఫసల్ బీమా యోజన (PMFBY)",
            "desc": "పంట నష్టానికి బీమా రక్షణ",
            "link": "https://pmfby.gov.in"
        },
        {
            "name": "PM-KISAN",
            "desc": "₹6000 ఆర్థిక సహాయం రైతులకు",
            "link": "https://pmkisan.gov.in"
        },
        {
            "name": "PM Kisan Maandhan Yojana",
            "desc": "వృద్ధాప్యంలో ₹3000 పెన్షన్",
            "link": "https://pmkmy.gov.in"
        }
    ]
    for disease in disease_info
}

# =========================
# USER INPUT
# =========================
disease = st.selectbox("🌾 పంట స్థితి ఎంచుకోండి", list(disease_info.keys()))

# =========================
# OUTPUT
# =========================
if disease:
    st.subheader("🌱 మీరు ఎంచుకున్నది")
    st.success(disease)

    st.subheader("🧠 రైతు సలహాలు")
    for tip in disease_info[disease]["tips"]:
        if "⚡" in tip:
            st.error(tip)
        else:
            st.write("• " + tip)

    st.subheader("🌟 ప్రో చిట్కాలు")
    for p in disease_info[disease]["pro_tips"]:
        st.info("👉 " + p)

    st.subheader("🛡 ప్రభుత్వ పథకాలు")
    for scheme in insurance_schemes[disease]:
        st.info(f"{scheme['name']} - {scheme['desc']}")
        st.markdown(f"[🔗 ఇక్కడ క్లిక్ చేయండి]({scheme['link']})")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("🚜 రైతు AI | స్మార్ట్ వ్యవసాయం 🌾")