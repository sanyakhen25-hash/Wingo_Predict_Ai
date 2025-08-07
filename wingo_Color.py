import streamlit as st

# Wingo analyzer logic
def get_result_from_game_number(game_number):
    if not game_number.isdigit() or len(game_number) != 17:
        return {"error": "Game number must be a 17-digit numeric value."}

    result_digit = int(game_number[-1])
    size = "Big" if result_digit >= 5 else "Small"

    if result_digit in [0, 5]:
        color = "Violet (also Green)"
    elif result_digit in [1, 3, 7, 9]:
        color = "Green"
    elif result_digit in [2, 4, 6, 8]:
        color = "Red"
    else:
        color = "Unknown"

    return {
        "Game Number": game_number,
        "Result Digit": result_digit,
        "Big/Small": size,
        "Color": color
    }

# Streamlit UI
st.set_page_config(page_title="Wingo Result Checker", page_icon="🎮", layout="centered")
st.title("Wingo Game Result Checker")
st.markdown("Enter the 17-digit game number to view the result.")

game_number = st.text_input("Game Number", max_chars=17)

if st.button("Check Result"):
    result = get_result_from_game_number(game_number)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Result Found!")
        st.write("Game Number:", result["Game Number"])
        st.write("Result Digit:", result["Result Digit"])
        st.write("Big/Small:", result["Big/Small"])
        st.write("Color:", result["Color"])