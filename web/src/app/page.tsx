"use client";

import { useEffect, useState } from "react";
import { getPrisioneros, searchPrisioneros } from "@/api/api";
import { Prisionero } from "../types/prisionero";

export default function Home() {
  const [prisioneros, setPrisioneros] = useState<Prisionero[]>([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    getPrisioneros().then(setPrisioneros);
  }, []);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (search.trim() === "") {
      getPrisioneros().then(setPrisioneros);
    } else {
      const data = await searchPrisioneros(search);
      setPrisioneros(data);
    }
  };

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Lista de Prisioneros</h1>

      <form onSubmit={handleSearch} className="mb-4 flex gap-2">
        <input
          type="text"
          placeholder="Buscar por palabra clave..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="border p-2 flex-1"
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded">
          Buscar
        </button>
      </form>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th className="border px-2 py-1">ID</th>
            <th className="border px-2 py-1">Fecha</th>
            <th className="border px-2 py-1">País</th>
            <th className="border px-2 py-1">Consulado</th>
            <th className="border px-2 py-1">Delito</th>
            <th className="border px-2 py-1">Cantidad</th>
            <th className="border px-2 py-1">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {prisioneros.map((p) => (
            <tr key={p.id} className="hover:bg-gray-100">
              <td className="border px-2 py-1">{p.id}</td>
              <td className="border px-2 py-1">{p.fecha_publicacion}</td>
              <td className="border px-2 py-1">{p.pais_prision}</td>
              <td className="border px-2 py-1">{p.consulado}</td>
              <td className="border px-2 py-1">{p.delito}</td>
              <td className="border px-2 py-1 text-center">{p.cantidad}</td>
              <td className="border px-2 py-1 text-center">
                <a href={`/prisionero/${p.id}`} className="text-blue-600 underline">
                  Ver Detalles
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
