# **Integración de Stripe (Modo Test).**
En este proyecto, se ha integrado Stripe en modo de prueba para gestionar pagos en línea de manera segura y efectiva. Este modo permite simular transacciones **sin realizar pagos reales**, lo que facilita el desarrollo y prueba de la funcionalidad de pago antes de un despliegue en producción.

Los datos del carrito, como el nombre, la cantidad y el precio de cada producto, se envían a Stripe para procesar la transacción. El flujo de pago incluye páginas configuradas para redirigir al usuario según el resultado del proceso: una página de éxito para pagos completados y otra de error en caso de fallos.

## Modo de prueba de Stripe.
El modo de prueba de Stripe incluye una serie de tarjetas de crédito de ejemplo para simular diferentes escenarios de pago, como transacciones exitosas, fondos insuficientes, tarjetas robadas y autenticación 3D Secure. Todas estas tarjetas son simuladas y no generan transacciones reales.

| **Tipo de Tarjeta**           | **Número de Tarjeta**       | **Resultado**                               |
|-------------------------------|-----------------------------|---------------------------------------------|
| **Tarjeta Genérica Exitosa**  | `4242 4242 4242 4242`       | Pago exitoso                                |
| **Tarjeta Rechazada**         | `4000 0000 0000 0002`       | Pago rechazado                              |
| **Fondos Insuficientes**      | `4000 0000 0000 9995`       | Pago fallido por falta de fondos            |
| **Tarjeta Robada**            | `4000 0000 0000 9987`       | Pago fallido debido a tarjeta robada        |
| **Tarjeta Expirada**          | `4000 0000 0000 0069`       | Pago fallido debido a expiración de tarjeta |
| **3D Secure Exitosa**         | `4000 0025 0000 3155`       | Solicita autenticación adicional y aprueba  |
| **3D Secure Fallida**         | `4000 0027 6000 3184`       | Solicita autenticación adicional, pero falla |

En todos los casos, se debe inventar el correo electrónico, el nombre del titular de la tarjeta, el CVV y la fecha de expiración para completar el formulario de pago. Por ejemplo, usar `test@example.com` como correo electrónico, `John Doe` como nombre del titular, `123` como CVV y cualquier fecha futura válida como fecha de expiración.

Para más información sobre el modo de prueba y las tarjetas de ejemplo de Stripe, se puede consultar a través de la documentación oficial de Stripe: [Stripe Documentation](https://docs.stripe.com/)
