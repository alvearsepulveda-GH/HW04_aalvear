# tarea04

**Curso**: Machine Learning Aplicado a las Finanzas - USACH

## Objetivo

Base de trabajo para desarrollar la Tarea 04 con una estructura simple y ordenada.

## Puesta en marcha

```bash
conda env create -f environment.yml
conda activate tarea04
jupyter lab
```

## Estructura de trabajo

```text
data/
  raw/          Datos originales
  processed/    Datos limpios o transformados
  external/     Fuentes auxiliares
notebooks/      Exploracion, pruebas y analisis
src/tarea04/    Codigo reutilizable del proyecto
models/         Modelos entrenados y artefactos
reports/        Graficos, tablas y entregables
tests/          Pruebas rapidas del proyecto
_legacy/        Material recuperado de versiones anteriores
```

## Flujo sugerido

1. Dejar los datos originales en `data/raw/`.
2. Hacer exploracion en `notebooks/`.
3. Mover la logica estable a `src/tarea04/`.
4. Guardar salidas finales en `reports/` y `models/`.
