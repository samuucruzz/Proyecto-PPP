> [!WARNING]
> Apartado de keepalived actualizado en el Google Docs

# Proyecto-IPTVilladeAgüimes
<div align="center">

<img src="assets/logo_iptv.jpeg" width="420">

# 📺 Streaming IPTVilladeaguimes

### Sistema de Streaming IPTV interno para distribución de contenido informativo

Infraestructura de streaming diseñada para **automatizar la reproducción de vídeos informativos en las televisiones del centro**, eliminando la necesidad de utilizar dispositivos USB y mejorando la gestión del contenido multimedia.

</div>

---

# ⚙️ Stack tecnológico del proyecto

<table>
<tr>
<td align="center" width="160">

**Sistema Operativo**

🐧
Ubuntu Server

</td>

<td align="center" width="160">

**Servidor Multimedia**

🎬
Jellyfin

</td>

<td align="center" width="160">

**Generador IPTV**

📡
ErsatzTV

</td>

<td align="center" width="160">

**Alta Disponibilidad**

🔁
Keepalived

</td>

<td align="center" width="160">

**Monitorización**

📊
Nagios

</td>

<td align="center" width="160">

**Almacenamiento**

💾
NAS

</td>

</tr>
</table>

---

# 📖 Descripción del proyecto

Actualmente, la actualización de los vídeos informativos del centro requiere un proceso manual que implica desplazarse físicamente hasta las televisiones situadas en los extremos del centro para copiar los vídeos mediante un **pendrive** y reiniciar la reproducción manualmente.

Este procedimiento presenta varios inconvenientes:

* ⏳ Pérdida de tiempo al desplazarse
* 🔌 Dependencia de dispositivos USB
* ⚙️ Falta de automatización del proceso
* 📂 Gestión poco eficiente del contenido multimedia

El proyecto **Streaming IPTVilladeaguimes** propone una solución basada en **streaming IPTV interno**, permitiendo gestionar los vídeos desde un servidor centralizado y reproducirlos automáticamente en las televisiones del centro.

---

# 🎯 Objetivos

## Objetivo principal

Implementar un sistema de **streaming interno centralizado** que permita distribuir vídeos informativos de forma rápida, sencilla y eficiente dentro de la red del centro.

## Objetivos específicos

* Eliminar el uso de **pendrives** para actualizar contenido
* Centralizar la **gestión de vídeos**
* Permitir una **actualización rápida del contenido**
* Garantizar **alta disponibilidad del servicio**
* Implementar **monitorización del sistema** para detectar fallos

---

# 🏗 Arquitectura del sistema

El sistema está compuesto por **tres máquinas virtuales con Ubuntu Server**, cada una con una función específica dentro de la infraestructura.

| Máquina           | Función                         | Servicios          |
| ----------------- | ------------------------------- | ------------------ |
| 🖥 MASTER         | Servidor principal de streaming | Jellyfin, ErsatzTV |
| 🗄 BACKUP         | Servidor de alta disponibilidad | Keepalived         |
| 📊 MONITORIZACIÓN | Supervisión del sistema         | Nagios             |

Esta arquitectura permite disponer de **un sistema estable, monitorizado y con alta disponibilidad** dentro de la red del centro.

---

# 🖥 Infraestructura

## Servidor MASTER

El servidor **MASTER** es el encargado de ejecutar los servicios principales del sistema de streaming.

### Servicios instalados

**Jellyfin**

Servidor multimedia encargado de gestionar la biblioteca de vídeos y organizar el contenido multimedia.

**ErsatzTV**

Herramienta que permite generar **canales IPTV virtuales** a partir de los contenidos multimedia disponibles.

Este servidor distribuye los vídeos mediante **streaming dentro de la red local** hacia las televisiones del centro.

---

## 🗄 Servidor BACKUP

El servidor **BACKUP** se encarga de garantizar la continuidad del servicio en caso de fallo del servidor principal.

### Servicio instalado

**Keepalived**

Permite implementar un sistema de **failover automático**, de forma que si el servidor MASTER deja de funcionar, el servidor BACKUP puede asumir automáticamente el servicio.

Esto proporciona **alta disponibilidad del sistema de streaming**.

---

# 📊 Servidor de monitorización

El servidor de **MONITORIZACIÓN** supervisa el estado de los servidores del sistema.

### Servicio instalado

**Nagios**

Funciones principales:

* Monitorizar el estado de los servidores
* Detectar si una máquina está **UP o DOWN**
* Identificar rápidamente fallos en la infraestructura

Esto permite mantener el sistema bajo supervisión constante y reaccionar rápidamente ante posibles incidencias.

---

# 💾 Almacenamiento de contenidos

Los vídeos utilizados para el sistema de streaming **se almacenan en un NAS (Network Attached Storage)** conectado a la red del centro.

El uso de un NAS permite:

* 📂 Centralizar el almacenamiento de contenidos
* 📈 Aumentar la capacidad de almacenamiento
* 🔄 Facilitar la actualización de vídeos
* ⚙️ Separar almacenamiento y procesamiento del streaming

Los servidores acceden al NAS para obtener los archivos multimedia que posteriormente se distribuyen mediante streaming.

---

# 🧰 Tecnologías utilizadas

| Tecnología         | Función                             |
| ------------------ | ----------------------------------- |
| Ubuntu Server      | Sistema operativo de los servidores |
| Jellyfin           | Gestión de contenido multimedia     |
| ErsatzTV           | Generación de canales IPTV          |
| Keepalived         | Alta disponibilidad                 |
| Nagios             | Monitorización                      |
| NAS                | Almacenamiento centralizado         |
| Máquinas virtuales | Infraestructura del proyecto        |

---

# 🚀 Resultados esperados

Con la implementación de este sistema se espera:

* Simplificar la gestión de los vídeos informativos
* Reducir el tiempo necesario para actualizar contenidos
* Eliminar la dependencia de dispositivos USB
* Mejorar la eficiencia del proceso de distribución de vídeos
* Disponer de una infraestructura **más moderna, automatizada y profesional**

---


# 👨‍💻 Autores

Proyecto académico desarrollado por:

**Samuel Cruz Lopez y**
**Simone Monzani Estevez**
- Alumnos del CIFP Villa de Agüimes, 2º del CFGS ASIR
