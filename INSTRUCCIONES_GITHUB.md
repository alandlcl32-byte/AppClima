# 📱 Instrucciones para generar tu APK con GitHub Actions

## Paso 1: Crear un repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre del repositorio: `WeatherApp` (o el que prefieras)
3. Marca como **Público** o **Privado** (ambos funcionan)
4. **NO** marques "Initialize with README"
5. Click en **Create repository**

## Paso 2: Subir tu proyecto a GitHub

Abre una terminal en la carpeta de tu proyecto y ejecuta:

```bash
cd /Users/mi00562/Downloads/WeatherApp/WeatherApp

# Inicializar git
git init

# Añadir todos los archivos
git add .

# Hacer el primer commit
git commit -m "Primera versión de WeatherApp"

# Conectar con tu repositorio (REEMPLAZA con tu URL)
git remote add origin https://github.com/TU_USUARIO/WeatherApp.git

# Crear rama main si no existe
git branch -M main

# Subir a GitHub
git push -u origin main
```

## Paso 3: Verificar que GitHub Actions esté compilando

1. Ve a tu repositorio en GitHub
2. Click en la pestaña **Actions**
3. Verás el workflow "Build Android APK" ejecutándose
4. Espera 15-20 minutos (primera vez puede tardar más)

## Paso 4: Descargar tu APK

Cuando termine la compilación:

1. En la pestaña **Actions**, click en el workflow completado (✓ verde)
2. Baja hasta **Artifacts**
3. Click en **WeatherApp-APK** para descargar
4. Descomprime el archivo ZIP
5. ¡Tendrás tu APK listo para instalar! 🎉

## Paso 5: Instalar en Android

1. Transfiere el APK a tu teléfono Android
2. Habilita "Instalar aplicaciones de origen desconocido"
3. Abre el APK y presiona Instalar

---

## 🔄 Compilaciones futuras

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

GitHub automáticamente compilará un nuevo APK.

---

## ⚠️ Nota importante

Si tu repositorio es PRIVADO, tienes límite de minutos gratuitos en GitHub Actions.
Si es PÚBLICO, tienes minutos ilimitados.

---

## 🆘 ¿Problemas?

Si la compilación falla:
1. Ve a Actions → Click en el workflow fallido
2. Revisa los logs en rojo para ver el error
3. La mayoría de errores son por permisos o dependencias faltantes en buildozer.spec
