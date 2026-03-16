# Proyecto-PPP
 Proyecto realizado por Samuel Cruz López y Simone Monzani Estevez
 Alumnado del CIFP Villa de Aguüimes.
 CGFS 2º ASIR

# Streaming IPTVilladeaguimes

Sistema de **streaming IPTV interno** diseñado para facilitar la gestión y reproducción de vídeos informativos en las televisiones del centro educativo sin necesidad de utilizar dispositivos USB.

Este proyecto implementa una infraestructura basada en **Ubuntu Server, alta disponibilidad y monitorización**, permitiendo administrar los contenidos de forma centralizada, eficiente y profesional.

---

# Descripción del proyecto

Actualmente, la actualización de los vídeos informativos del centro requiere un proceso manual que implica desplazarse físicamente hasta las televisiones con un pendrive para copiar los archivos y reiniciar la reproducción.

Este método presenta varios inconvenientes:

* Pérdida de tiempo.
* Dependencia de dispositivos USB.
* Gestión poco eficiente del contenido.
* Falta de automatización.

El proyecto **Streaming IPTVilladeaguimes** propone una solución basada en **streaming IPTV interno**, permitiendo gestionar los vídeos desde un servidor centralizado y reproducirlos automáticamente en las televisiones del centro.

---

# Objetivos

## Objetivo principal

Mejorar la gestión y distribución de los vídeos informativos mediante un sistema de streaming interno accesible desde la red del centro.

## Objetivos específicos

* Eliminar el uso de **pendrives** para actualizar contenido.
* Centralizar la **gestión de vídeos**.
* Permitir una **actualización rápida y sencilla** del contenido.
* Garantizar **alta disponibilidad** del servicio.
* Implementar **monitorización del sistema** para detectar fallos.

---

# Arquitectura del sistema

El sistema está compuesto por **tres máquinas virtuales con Ubuntu Server**, cada una con una función específica dentro de la infraestructura.

| Máquina        | Función                         | Servicios          |
| -------------- | ------------------------------- | ------------------ |
| MASTER         | Servidor principal de streaming | Jellyfin, ErsatzTV |
| BACKUP         | Servidor de alta disponibilidad | Keepalived         |
| MONITORIZACIÓN | Supervisión del sistema         | Nagios             |

---

# Infraestructura

## Servidor MASTER

El servidor **MASTER** es el encargado de ejecutar los servicios principales del sistema de streaming.

Servicios instalados:

* **Jellyfin**
  Servidor multimedia encargado de gestionar la biblioteca de vídeos.

* **ErsatzTV**
  Herramienta que permite generar **canales IPTV virtuales** a partir de los contenidos multimedia almacenados.

Este servidor distribuye el contenido mediante streaming a las televisiones conectadas a la red del centro.

---

## Servidor BACKUP

El servidor **BACKUP** garantiza la continuidad del servicio en caso de fallo del servidor principal.

Servicio instalado:

* **Keepalived**

Este servicio permite implementar un sistema de **failover**, de forma que si el servidor MASTER deja de funcionar, el servidor BACKUP puede asumir automáticamente el servicio.

Esto proporciona **alta disponibilidad del sistema** y evita interrupciones en la reproducción de los vídeos.

---

## Servidor de monitorización

El servidor de **MONITORIZACIÓN** supervisa el estado de los servidores del sistema.

Servicio instalado:

* **Nagios**

Nagios permite:

* Monitorizar el estado de los servidores.
* Detectar si un servicio o máquina se encuentra **UP o DOWN**.
* Identificar rápidamente fallos en la infraestructura.

---

# Almacenamiento de contenidos

Los vídeos utilizados para el sistema de streaming **no se almacenan directamente en los servidores**, sino en un **NAS (Network Attached Storage)** conectado a la red del centro.

Esto permite:

* Centralizar el almacenamiento de los vídeos.
* Facilitar la gestión del contenido.
* Aumentar la capacidad de almacenamiento.
* Separar el almacenamiento del procesamiento del streaming.

Los servidores acceden al NAS para obtener los archivos multimedia que posteriormente se distribuyen mediante streaming.

---

# Tecnologías utilizadas

* Ubuntu Server
* Jellyfin
* ErsatzTV
* Keepalived
* Nagios
* NAS (Network Attached Storage)
* Virtualización mediante máquinas virtuales

---

# Resultados esperados

Con la implementación de este sistema se espera:

* Simplificar la gestión de los vídeos informativos.
* Reducir el tiempo necesario para actualizar contenidos.
* Eliminar la dependencia de dispositivos USB.
* Mejorar la eficiencia del proceso de distribución de vídeos.
* Disponer de una infraestructura más **moderna, automatizada y profesional**.
