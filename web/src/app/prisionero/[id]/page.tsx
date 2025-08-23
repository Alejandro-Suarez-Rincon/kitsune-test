"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { getPrisioneroById } from "@/api/api";

interface Prisionero {
  id: number;
  fecha_publicacion: string;
  pais_prision: string;
  consulado: string;
  delito: string;
  extraditado: string;
  situacion_juridica: string;
  genero: string;
  grupo_edad: string;
  cantidad: number;
  latitud: number;
  longitud: number;
}

export default function PrisioneroDetalle() {
  const { id } = useParams<{ id: string }>();
  const router = useRouter();
  const [prisionero, setPrisionero] = useState<Prisionero | null>(null);

  useEffect(() => {
    if (id) {
      getPrisioneroById(id).then(setPrisionero);
    }
  }, [id]);

  if (!prisionero) return <p className="p-4">Cargando...</p>;

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Detalle del Prisionero #{prisionero.id}</h1>
      <ul className="space-y-2">
        <li><strong>Fecha publicación:</strong> {prisionero.fecha_publicacion}</li>
        <li><strong>País:</strong> {prisionero.pais_prision}</li>
        <li><strong>Consulado:</strong> {prisionero.consulado}</li>
        <li><strong>Delito:</strong> {prisionero.delito}</li>
        <li><strong>Extraditado:</strong> {prisionero.extraditado}</li>
        <li><strong>Situación jurídica:</strong> {prisionero.situacion_juridica}</li>
        <li><strong>Género:</strong> {prisionero.genero}</li>
        <li><strong>Grupo de edad:</strong> {prisionero.grupo_edad}</li>
        <li><strong>Cantidad:</strong> {prisionero.cantidad}</li>
        <li><strong>Ubicación:</strong> ({prisionero.latitud}, {prisionero.longitud})</li>
      </ul>
      <button
        className="mt-4 bg-gray-600 text-white px-4 py-2 rounded"
        onClick={() => router.back()}
      >
        Volver
      </button>
    </div>
  );
}
