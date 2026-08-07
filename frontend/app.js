const input = document.querySelector("#text-input");
const button = document.querySelector("#predict-button");
const status = document.querySelector("#status");
const resultSection = document.querySelector("#result");
const sentimentValue = document.querySelector("#sentiment-value");
const confidenceValue = document.querySelector("#confidence-value");
const scorePositive = document.querySelector("#score-positive");
const scoreNeutral = document.querySelector("#score-neutral");
const scoreNegative = document.querySelector("#score-negative");
const scoreCompound = document.querySelector("#score-compound");

const API_URL = "/predict";

function setStatus(message, isError = false) {
  status.textContent = message;
  status.style.color = isError ? "#fda4af" : "#94a3b8";
}

function showResult(data) {
  sentimentValue.textContent = data.sentiment;
  confidenceValue.textContent = `${Math.round(data.confidence * 100)}%`;
  scorePositive.textContent = data.scores.positive.toFixed(3);
  scoreNeutral.textContent = data.scores.neutral.toFixed(3);
  scoreNegative.textContent = data.scores.negative.toFixed(3);
  scoreCompound.textContent = data.scores.compound.toFixed(3);
  resultSection.classList.remove("hidden");
}

async function handleSubmit() {
  const text = input.value.trim();
  if (!text) {
    setStatus("Please enter some text before predicting.", true);
    return;
  }

  button.disabled = true;
  setStatus("Analyzing text...", false);
  resultSection.classList.add("hidden");

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Prediction error");
    }

    const data = await response.json();
    showResult(data);
    setStatus("Prediction complete.");
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    button.disabled = false;
  }
}

button.addEventListener("click", handleSubmit);
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && event.shiftKey === false) {
    event.preventDefault();
    handleSubmit();
  }
});
