const API_URL = "http://localhost:8001";

export async function getPrisioneros() {
  const res = await fetch(`${API_URL}/prisioneros/`, { cache: "no-store" });
  return res.json();
}

export async function searchPrisioneros(palabra: string) {
  const res = await fetch(`${API_URL}/prisioneros/buscar/${palabra}`, { cache: "no-store" });
  return res.json();
}

export async function getPrisioneroById(id: string) {
  const res = await fetch(`${API_URL}/prisioneros/${id}`, { cache: "no-store" });
  return res.json();
}
