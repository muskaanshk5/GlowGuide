import streamlit as st

def get_recommendations(skin_type):
    recommendations = {
        "oily": ["Oil-Free Face Wash", "Matte Moisturizer", "Charcoal Face Mask"],
        "dry": ["Hydrating Serum", "Deep Moisturizer", "Hyaluronic Acid Mask"],
        "sensitive": ["Gentle Cleanser", "Fragrance-Free Moisturizer", "Aloe Vera Gel"]
    }
    return recommendations.get(skin_type, ["General Skincare Routine"])

def recommendation():
    st.title("Personalized Skincare Recommendations")
    skin_type = st.selectbox("Select your skin type", ["oily", "dry", "sensitive"])

    if st.button("Show Recommendations"):
        products = get_recommendations(skin_type)
        for product in products:
            st.write(f"- {product}")

if __name__ == "__main__":
    recommendation()
