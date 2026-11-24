<div align="center">

# Cuttlefish-1C-test

**Пример работы с LUA-скриптами для статьи на INFOSTART.RU**

[![INFOSTART](https://infostart.ru/bitrix/templates/sandbox_empty/assets/tpl/abo/img/logo.svg)](https://infostart.ru)

</div>

---

Использование внешнего LUA движка для выполнения сложной бизнес-логики в связке с 1С:Предприятие. 

В статье на Инфостарте рассматривается, как с помощью ETL-инструмента Cuttlefish вынести ресурсоемкие расчеты, парсинг данных и трансформации из закрытого языка 1С в быстрые скрипты Lua, не снимая конфигурацию с поддержки.

📖 **Читать статью:** [Использование внешнего LUA движка для 1С](https://infostart.ru/1c/articles/2855198/)

## Быстрый старт

```bash
git clone https://github.com/CuttlefishETL/cuttlefish_ts_ui.git
cd cuttlefish_ts_ui
npm install
npm run tauri dev
