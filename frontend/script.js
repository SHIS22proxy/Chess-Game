async function makeMove(from, to) {
  const response = await fetch('/move', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ from, to })
  });
  const result = await response.json();
  console.log(result);
}

async function makeAIMove() {
  const response = await fetch('/ai-move');
  const move = await response.json();
  console.log("AI Move:", move);
}
