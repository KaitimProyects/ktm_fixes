# ktm_fixes

Repositorio de módulos de corrección temporal para bugs conocidos en Odoo core. Cada módulo dentro de este repositorio es un parche aislado que se elimina en cuanto Odoo publica la solución oficial.

## Convención

- **Un módulo por dominio** (MRP, contabilidad, inventario, etc.).
- Cada fix lleva en su XML/Python un comentario con el commit o issue upstream de referencia.
- Cuando Odoo resuelva el bug: se elimina el record/código del fix y se archiva la entrada en la sección "Removed Fixes" del `static/description/index.html` del módulo.

## Módulos

| Módulo | Descripción | Depende de |
|--------|-------------|------------|
| [ktm_mrp_fixes](ktm_mrp_fixes/) | Fixes temporales para el módulo MRP de Odoo | `mrp` |

## Instalación

1. Asegurarse de que este repositorio esté en el addons path de Odoo.
2. Actualizar lista de apps: **Apps → Actualizar lista de aplicaciones**.
3. Instalar el módulo correspondiente desde Apps.

## Agregar un fix nuevo

1. Identificar el módulo de dominio correcto (o crear uno nuevo si no existe).
2. Agregar el fix mínimo necesario en `views/`, `models/`, etc.
3. Documentar en el XML/Python: commit upstream de referencia y condición de remoción.
4. Actualizar la sección **Active Fixes** en `static/description/index.html` del módulo.
5. Actualizar la tabla de módulos en este README si se crea un módulo nuevo.

---

**Autor:** Kaitim S.A. de C.V. — [kaitim.com](https://www.kaitim.com)
