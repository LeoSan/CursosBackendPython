# ☁️ Guía de Estudio: Fundamentos y Arquitectura Cloud
Este documento resume los conceptos clave de arquitectura agnóstica, serverless, contenedores y buenas prácticas en la nube revisados durante el simulacro.
---
## 1. Fundamentos y Costos
*   **Modelo de Pago:** En la nube se paga por **uso granular** (minutos o segundos).
*   **Facturación de Funciones (FaaS):** Se mide por **memoria aprovisionada**, **cantidad de ejecuciones** y **tiempo de ejecución**.
*   **Elasticidad:** Es la capacidad de crecer y **decrementar** recursos automáticamente. Es vital reducir recursos al estado original tras un pico para **optimizar costos**.
*   **Límites de Servicio:** Para ampliar los límites impuestos por el proveedor (cuotas), se debe abrir un **Caso de Soporte**.
## 2. Arquitectura y Capas
El flujo de una petición en una arquitectura agnóstica sigue este orden:
1.  **DNS:** Resolución del dominio.
2.  **CDN / WAF:** Entrega de contenido y filtrado de seguridad (Edge).
3.  **Balanceador / API Gateway:** Distribución de carga.
4.  **Autenticación:** Validación de identidad.
5.  **Backend (Zona Privada):** Lógica de negocio segura.
## 3. Serverless (Arquitectura sin Servidores)
*   **Componentes:** El flujo estándar es: `API Gateway` → `Función (Lambda)` → `Datastore (DB)`.
*   **Exposición:** Una función se expone al mundo exterior principalmente a través de un **API Gateway**.
*   **Vendor Lock-in:** Migrar funciones entre nubes (ej. Azure a AWS) es costoso porque los servicios varían; a menudo implica **rehacer la integración** de la aplicación.
## 4. Contenedores y Escalabilidad
*   **Kubernetes:** El orquestador estándar "Cloud Native".
*   **Placement:** Estrategia para decidir en qué nodo físico se ejecuta un contenedor.
*   **Niveles de Escalabilidad:**
    *   **Escalabilidad del Microservicio:** Crear más réplicas del contenedor.
    *   **Escalabilidad del Clúster:** Añadir más servidores (nodos) físicos/virtuales a la infraestructura.
## 5. Alta Disponibilidad (HA) y Resiliencia
*   **Multi-AZ:** Característica que añade **Alta Disponibilidad** real al distribuir recursos en diferentes zonas de disponibilidad dentro de una región.
*   **Soberanía de Datos:** Si el Estado exige que los datos no salgan del país, la solución es elegir un proveedor con **Data Center Local**.
*   **Retraso en Escalamiento:** Durante un pico repentino, los usuarios pueden ver errores aunque el escalamiento "funcione bien". Esto se debe al **tiempo de aprovisionamiento** (booting y health checks) de los nuevos servidores.
## 6. Conceptos Avanzados
*   **Machine Learning en la Nube:** Ideal para iniciar rápido y con baja inversión porque evita la compra de hardware costoso (GPU) y ofrece servicios listos para usar (**OpEx**).
*   **AMI (Amazon Machine Image):** Imagen base con software preinstalado usada para lanzar nuevos nodos idénticos.
*   **Round-robin:** Algoritmo básico de balanceo que distribuye tráfico secuencialmente.
💡 Tips para tu examen:
Diferencia siempre entre Horizontal y Vertical: Horizontal es añadir más máquinas (nubes modernas), Vertical es hacer más grande una sola máquina (vieja escuela).
Recuerda el "Edge": Todo lo que sea seguridad inicial (WAF) y velocidad (CDN) ocurre antes de que la petición toque tu servidor.
Sigue el dinero: Muchas respuestas correctas se basan en "ahorrar costos" u "optimizar el pago por uso".
¡Mucho éxito con ese certificado, Leonard! Si necesitas profundizar en algún punto o tienes más preguntas, aquí estoy. 🚀