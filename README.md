# Proyecto-PPP
<div align="center">

# 📺 Streaming IPTVilladeaguimes

### Sistema de Streaming IPTV interno para distribución de contenido informativo

![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![Jellyfin](https://img.shields.io/badge/Jellyfin-Media%20Server-00A4DC?style=for-the-badge)
![Nagios](https://img.shields.io/badge/Nagios-Monitoring-000000?style=for-the-badge)
![Keepalived](https://img.shields.io/badge/Keepalived-High%20Availability-blue?style=for-the-badge)
![IPTV](https://img.shields.io/badge/IPTV-Streaming-purple?style=for-the-badge)

Sistema diseñado para **gestionar y reproducir vídeos informativos en las televisiones del centro educativo mediante streaming**, eliminando la necesidad de utilizar dispositivos USB.

</div>

---

# 📖 Descripción del proyecto

Actualmente, la actualización de los vídeos informativos del centro requiere un proceso manual que implica:

* Desplazarse físicamente hasta las televisiones.
* Utilizar un **pendrive** para copiar los vídeos.
* Reiniciar manualmente la reproducción.

Este método genera varios problemas:

* ⏳ Pérdida de tiempo
* 🔌 Dependencia de dispositivos USB
* ⚙️ Falta de automatización
* 📂 Gestión poco eficiente del contenido

El proyecto **Streaming IPTVilladeaguimes** propone una solución basada en **streaming IPTV interno**, permitiendo gestionar los vídeos desde un servidor centralizado y reproducirlos automáticamente en las televisiones del centro.

---

# 🎯 Objetivos

## Objetivo principal

Implementar un sistema de **streaming interno centralizado** que permita distribuir vídeos informativos de forma rápida, sencilla y eficiente.

## Objetivos específicos

* Eliminar el uso de **pendrives** para actualizar contenido.
* Centralizar la **gestión de vídeos**.
* Permitir una **actualización rápida del contenido**.
* Garantizar **alta disponibilidad del servicio**.
* Implementar **monitorización del sistema** para detectar fallos.

---

# 🏗 Arquitectura del sistema

El sistema está compuesto por **tres máquinas virtuales con Ubuntu Server**, cada una con una función específica dentro de la infraestructura.

| Máquina           | Función                         | Servicios          |
| ----------------- | ------------------------------- | ------------------ |
| 🖥 MASTER         | Servidor principal de streaming | Jellyfin, ErsatzTV |
| 🗄 BACKUP         | Servidor de alta disponibilidad | Keepalived         |
| 📊 MONITORIZACIÓN | Supervisión del sistema         | Nagios             |

Esta arquitectura permite disponer de **servicio continuo y supervisado** dentro de la red del centro.

---

# 🖥 Infraestructura

## Servidor MASTER

El servidor **MASTER** ejecuta los servicios principales responsables del streaming.

**Servicios instalados**

* **Jellyfin**
  Servidor multimedia encargado de gestionar la biblioteca de vídeos.

* **ErsatzTV**
  Herramienta que permite generar **canales IPTV virtuales** a partir del contenido multimedia.

Este servidor distribuye los vídeos mediante **streaming dentro de la red local** hacia las televisiones del centro.

---

## 🗄 Servidor BACKUP

El servidor **BACKUP** garantiza la continuidad del servicio en caso de fallo del servidor principal.

**Servicio instalado**

* **Keepalived**

Este sistema implementa un mecanismo de **failover automático**, permitiendo que el servidor backup asuma el control si el servidor principal deja de funcionar.

Esto asegura una **alta disponibilidad del sistema de streaming**.

---

## 📊 Servidor de monitorización

El servidor de **MONITORIZACIÓN** supervisa el estado de los servidores del sistema.

**Servicio instalado**

* **Nagios**

Funciones principales:

* Monitorizar el estado de los servidores.
* Detectar si un sistema está **UP o DOWN**.
* Identificar posibles fallos en la infraestructura.

---

# 💾 Almacenamiento de contenidos

Los vídeos utilizados para el sistema de streaming se almacenan en un **NAS (Network Attached Storage)** conectado a la red del centro.

Esto permite:

* 📂 Centralizar el almacenamiento de contenidos.
* 📈 Aumentar la capacidad de almacenamiento.
* 🔄 Facilitar la actualización de vídeos.
* ⚙️ Separar almacenamiento y procesamiento.

Los servidores acceden al NAS para obtener los vídeos que posteriormente se distribuyen mediante streaming.

---

# 🧰 Tecnologías utilizadas

| Tecnología             | Función                             |
| ---------------------- | ----------------------------------- |
| **Ubuntu Server**      | Sistema operativo de los servidores |
| **Jellyfin**           | Gestión de contenido multimedia     |
| **ErsatzTV**           | Generación de canales IPTV          |
| **Keepalived**         | Alta disponibilidad (Failover)      |
| **Nagios**             | Monitorización de servidores        |
| **NAS**                | Almacenamiento centralizado         |
| **Máquinas Virtuales** | Infraestructura del proyecto        |

---

# 🚀 Resultados esperados

Con la implementación de este sistema se espera:

* Simplificar la gestión de los vídeos informativos.
* Reducir el tiempo necesario para actualizar contenido.
* Eliminar la dependencia de dispositivos USB.
* Mejorar la eficiencia del proceso de distribución de vídeos.
* Disponer de una infraestructura **moderna, automatizada y profesional**.

---

# 👨‍💻 Autores

Proyecto académico desarrollado por:

**Samuel**
**Simone**
- Alumnos del CIFP Villa de Agüimes, 2º del CFGS ASIR

---

<div align="center">

⭐ Proyecto desarrollado con fines educativos

</div>
