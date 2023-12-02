# Registro de Usuarios en FastAPI

## Descripción del Proyecto
Este proyecto implementa un sistema de registro de usuarios en una aplicación construida con FastAPI. Se enfoca en proporcionar un enfoque robusto y seguro para el registro de usuarios, cumpliendo con criterios específicos y utilizando buenas prácticas de desarrollo.

### Caso de Estudio
- **Objetivo**: Implementar un sistema de registro de usuarios que sea seguro, eficiente y cumpla con reglas de negocio específicas.
- **Reglas de Negocio**:
    - Solo mayores de 18 años pueden registrarse.
    - Se aceptan únicamente correos de Gmail.
    - Los usuarios deben residir en Chile.
    - La contraseña debe cumplir con los estándares de seguridad de OWASP.
    - Se envía un correo de confirmación tras el registro exitoso.
- **Datos del Perfil**:
    - Dirección completa, sexo, edad, estado civil, altura, peso.
    - Información sobre hijos (nombres, sexos, edades) y si viven con el usuario.
    - Posibilidad de agregar una foto de perfil.
## Instalación y Configuración

**Requisitos Previos:**
- Python 3.8 o superior.
- Cuenta AWS y configuración de AWS CLI.
- Herramientas serverless como AWS SAM o Framework Serverless.

**Configuración del Entorno:**
1. Clona el repositorio:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
2. Navega al directorio del proyecto y crea un entorno virtual:
   ```
   cd tu-repositorio
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Configura tus credenciales AWS y variables de entorno según sea necesario.

**Despliegue Serverless:**
- Utiliza AWS SAM o Framework Serverless para desplegar tu aplicación en AWS Lambda conectada con Amazon API Gateway y DynamoDB.

## Uso

**Interacción con la API:**

Una vez desplegada, la API estará accesible a través de la URL proporcionada por Amazon API Gateway.

- **Registro de Usuarios:**
  - Método: POST
  - Endpoint: `/register`
  - Body de ejemplo:
    ```json
    {
      "email": "user@example.com",
      "password": "your_secure_password"
    }
    ```

**Pruebas Locales:**

- Para pruebas locales, considera usar herramientas como SAM Local o localstack.

## Pruebas

```
pytest
```
