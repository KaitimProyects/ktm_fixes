# ktm_mrp_fixes

Fixes temporales para bugs conocidos en el módulo MRP de Odoo core.

## Fixes activos

### move_raw_ids truncado a 40 componentes

**Upstream:** commit `3d43d9d9` (PERF: respect limit during onchange fetch)  
**Agregado:** 2026-05-05  
**Archivo:** `views/mrp_production_views.xml`

Al crear una orden de producción con una lista de materiales de más de 40 componentes, el onchange silenciosamente trunca `move_raw_ids` a los primeros 40. El commit upstream hizo que el backend respete el `limit` que envía el frontend (default 40), descartando el resto.

**Fix:** extiende `mrp.mrp_production_form_view` y sube el `limit` del widget `move_raw_ids` a 500.

**Remover cuando:** Odoo core establezca un límite por defecto razonable o exponga una clave de configuración para esto.

---

## Fixes removidos

_(ninguno aún)_

---

## Agregar un fix nuevo

1. Crear el archivo mínimo necesario en `views/`, `models/`, etc.
2. Documentar dentro del archivo: commit/issue upstream y condición de remoción.
3. Agregar una entrada en **Fixes activos** arriba.
4. Actualizar la tabla en `static/description/index.html`.
