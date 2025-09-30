const form = document.getElementById('diagForm');
const resultDiv = document.getElementById('result');
const diffsDiv = document.getElementById('diffs');
const interactionsDiv = document.getElementById('interactions');
const referralDiv = document.getElementById('referral');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const payload = {
    symptoms: document.getElementById('symptoms').value.trim(),
    history: document.getElementById('history').value.trim(),
    vitals: '',
    meds: document.getElementById('meds').value
      ? document.getElementById('meds').value.split(",").map(s => s.trim())
      : [],
    patient: {
      name: document.getElementById('p_name').value.trim() || null,
      age: Number(document.getElementById('p_age').value) || null,
      gender: document.getElementById('p_gender').value || null
    }
  };

  resultDiv.style.display = 'block';
  diffsDiv.innerHTML = "<p>Loading results...</p>";
  interactionsDiv.innerHTML = "";
  referralDiv.innerHTML = "";

  try {
    const res = await fetch('http://192.168.165.231:8000/diagnose', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Server error ${res.status}: ${text}`);
    }

    const data = await res.json();
    showResult(data);

  } catch (err) {
    alert("Failed to get diagnosis:\n" + (err.message || err));
  }
});

function showResult(result) {
  diffsDiv.innerHTML = "<h3>Differential Diagnoses</h3>";
  if (!result.differential || result.differential.length === 0) {
    diffsDiv.innerHTML += "<p>No likely matches found.</p>";
  } else {
    result.differential.forEach(d => {
      diffsDiv.innerHTML += `<div style="border-bottom:1px solid #eee; padding:8px 0;">
        <b>${d.disease}</b> — Confidence: ${d.confidence}<br/>
        Severity: ${d.severity}<br/>
        <small>${d.summary || 'No summary'}</small>
      </div>`;
    });
  }

  interactionsDiv.innerHTML = "<h3>Drug Interactions</h3>";
  if (result.drug_interactions && result.drug_interactions.length) {
    result.drug_interactions.forEach(i => interactionsDiv.innerHTML += `<div>${i}</div>`);
  } else interactionsDiv.innerHTML += "<p>No known interactions.</p>";

  referralDiv.innerHTML = `<h3>Referral</h3>
    <p>${result.referral_recommended ? 'Recommend specialist referral / urgent action' : 'Manage locally'}</p>`;
}
