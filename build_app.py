import json

BARTER_DATA = [
    {"faction": "all", "category": "Оружие", "name": "АК-15", "role": "Универсал / PvP / Открытый мир (Мастер)",
     "steps": [{"stage": "Новичок", "item": "АК-74М", "cost": "Болота / Кордон"},
               {"stage": "Сталкер", "item": "АК-103", "cost": "Бар и Свалка"},
               {"stage": "Ветеран", "item": "АК-203", "cost": "Север + Батареи / Маячки"},
               {"stage": "Мастер", "item": "АК-15", "cost": "Топ Север + Сыворотки"}],
     "attachments": ["Прицел: Elcan / Sig Sauer Romeo / Barska", "Надульник: Глушитель АТГ / Тактический ДТК",
                     "Цевье: Зенит Б-30", "Рукоятка: Magpul AFG / РК-1", "Магазин: 40-45 пат. (7.62)", "Приклад: Зенит ПТ-3"],
     "tip": "Лучший баланс урона и цены патронов."},
    {"faction": "all", "category": "Оружие", "name": "ПКП «Печенег»", "role": "PvE / Данжи / Споты (Мастер)",
     "steps": [{"stage": "Сталкер", "item": "РПД", "cost": "Ресурсы Бара"},
               {"stage": "Ветеран", "item": "Поношенный ПКП", "cost": "Армейские склады / Север"},
               {"stage": "Мастер", "item": "ПКП «Печенег»", "cost": "Север + Сыворотки"}],
     "attachments": ["Прицел: 1x коллиматор (EOTech)", "Надульник: Тяжелый ДТК", "Кронштейн: Зенит Б-50",
                     "Рукоятка: На контроль отдачи", "Тактический блок: ЛЦУ (для стрельбы от бедра)"],
     "tip": "Короб на 100-200 патронов избавляет от перезарядки, но режет скорость бега."},
    {"faction": "all", "category": "Оружие", "name": "А-545", "role": "Агрессивное PvP в упор (Мастер)",
     "steps": [{"stage": "Ветеран", "item": "АЕК-971", "cost": "Север + Маячки"},
               {"stage": "Мастер", "item": "А-545", "cost": "Топ Север + Сыворотки"}],
     "attachments": ["Прицел: Panorama / Barska", "Надульник: Глушитель 5.45 / Компенсатор",
                     "Рукоятка: На скорость прицеливания", "Магазин: Барабан на 60 пат. (5.45)"],
     "tip": "Бешеная скорострельность вблизи, но быстро тратит боезапас."},
    {"faction": "all", "category": "Вторичное", "name": "Protecta", "role": "Защита от мутантов (Мастер)",
     "steps": [{"stage": "Новичок", "item": "МР-133", "cost": "Кордон"},
               {"stage": "Сталкер", "item": "МР-153", "cost": "Бар"},
               {"stage": "Ветеран", "item": "Сайга-12К", "cost": "Север"},
               {"stage": "Мастер", "item": "Protecta", "cost": "Север + Сыворотки"}],
     "attachments": ["Надульник: Чок / Получок", "Тактический блок: Мощный ЛЦУ"],
     "tip": "На Ветеране Сайга-12К с магазинами на 8-10 патронов закрывает 90% задач."},
    {"faction": "stalker", "category": "Броня", "name": "Скат-10 / Мул (Сталкеры)", "role": "Комбинированная (Мастер)",
     "steps": [{"stage": "Новичок", "item": "Заря", "cost": "Болота / Кордон"},
               {"stage": "Сталкер", "item": "Скат-9б / Сокол", "cost": "Бар"},
               {"stage": "Мастер", "item": "Скат-10 / Мул", "cost": "Север + Сыворотки"}],
     "attachments": ["Пластины: Керамика / Сталь", "ПНВ: 2-3 поколение"],
     "tip": "Лучший первый костюм Мастера для Сталкера: баланс пулестойкости, веса и защиты."},
    {"faction": "bandit", "category": "Броня", "name": "Скат-10 / Туз (Бандиты)", "role": "Комбинированная (Мастер)",
     "steps": [{"stage": "Новичок", "item": "Бандитский плащ", "cost": "Болота / Кордон"},
               {"stage": "Сталкер", "item": "Пересмешник / Восход", "cost": "Бар"},
               {"stage": "Мастер", "item": "Скат-10 / Туз", "cost": "Север + Сыворотки"}],
     "attachments": ["Пластины: Керамика / Сталь", "ПНВ: 2-3 поколение"],
     "tip": "«Туз» — бандитский аналог «Мула» с отличным переносимым весом."},
    {"faction": "stalker", "category": "Броня", "name": "Центурион (Сталкеры)", "role": "Боевая для PvP (Мастер)",
     "steps": [{"stage": "Сталкер", "item": "Аврора", "cost": "Бар"},
               {"stage": "Ветеран", "item": "Гектор", "cost": "Север"},
               {"stage": "Мастер", "item": "Центурион", "cost": "Топ Север + Сыворотки"}],
     "attachments": ["Пластины: Тяжелые на пулестойкость", "ПНВ: Высокого тира"],
     "tip": "Максимум пулестойкости для PvP, но слабая защита от заражений."},
    {"faction": "bandit", "category": "Броня", "name": "Центурион (Бандиты)", "role": "Боевая для PvP (Мастер)",
     "steps": [{"stage": "Сталкер", "item": "Пахан / Легионер", "cost": "Бар"},
               {"stage": "Ветеран", "item": "Булат / Гектор", "cost": "Север"},
               {"stage": "Мастер", "item": "Центурион", "cost": "Топ Север + Сыворотки"}],
     "attachments": ["Пластины: Тяжелые на пулестойкость", "ПНВ: Высокого тира"],
     "tip": "На Севере ветка бандитов сходится в общий Центурион."},
    {"faction": "all", "category": "Броня", "name": "Сатурн (Общий)", "role": "Научная для заражений 3-4 ур. (Мастер)",
     "steps": [{"stage": "Сталкер", "item": "КИМ-99 «Малахит»", "cost": "Бар"},
               {"stage": "Ветеран", "item": "КИМ-122 «Аметист»", "cost": "Север"},
               {"stage": "Мастер", "item": "Сатурн", "cost": "Север + Сыворотки"}],
     "attachments": ["Пластины: Композитные", "Визор: Встроенный научный"],
     "tip": "Делается вторым костюмом для фарма архианомалий."},
    {"faction": "all", "category": "Контейнеры", "name": "Контейнер «Улей»", "role": "Эндгейм PvP — 5 слотов (Мастер)",
     "steps": [{"stage": "Сталкер", "item": "Берлога-4", "cost": "Бар"},
               {"stage": "Ветеран", "item": "Берлога-6", "cost": "Север"},
               {"stage": "Мастер", "item": "Контейнер «Улей»", "cost": "Топ Север + Сыворотки"}],
     "attachments": ["Сборка (5 сл.): 1x Атом + 4x Осколок / Солнце / Многогранник",
                     "На Берлогу-6: 2x Светляк + 2x Спираль + 2x Пузырь"],
     "tip": "Лучше гасит дебаффы топовых артефактов, чем Берлога-6."}
]
HTML = """<!DOCTYPE html>
<html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>STALZONE Бартер</title><style>
*{box-sizing:border-box;margin:0;padding:0;font-family:sans-serif}
body{background:#121417;color:#e5e7eb;padding:16px;max-width:850px;margin:auto}
h1{color:#f59e0b;text-align:center;font-size:1.3rem;margin-bottom:12px}
.dl-box{text-align:center;margin-bottom:14px}
.dl-btn{display:inline-block;padding:10px 16px;background:#22c55e;color:#000;font-weight:700;text-decoration:none;border-radius:8px;font-size:.9rem}
.factions{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px}
.f-btn{padding:10px;border-radius:8px;border:1px solid #2c323b;background:#1c2026;color:#9ca3af;font-weight:700;cursor:pointer}
.f-btn.active.stalker{background:#2563eb;color:#fff;border-color:#3b82f6}
.f-btn.active.bandit{background:#7c3aed;color:#fff;border-color:#8b5cf6}
input{width:100%;padding:10px;border-radius:8px;border:1px solid #2c323b;background:#1c2026;color:#fff;margin-bottom:10px}
.tabs{display:flex;gap:6px;overflow-x:auto;margin-bottom:16px}
.tab{padding:8px 12px;border-radius:6px;border:1px solid #2c323b;background:#1c2026;color:#9ca3af;cursor:pointer;white-space:nowrap}
.tab.active{background:#f59e0b;color:#000;font-weight:700}
.card{background:#1c2026;border:1px solid #2c323b;border-radius:10px;padding:14px;margin-bottom:14px}
.title{font-size:1.15rem;font-weight:700;color:#fff}.role{font-size:.85rem;color:#9ca3af;margin:4px 0 12px}
.tree{border-left:2px solid #f59e0b;padding-left:12px;margin-bottom:12px}
.step{margin-bottom:8px}.st{font-size:.75rem;font-weight:700;color:#f59e0b;text-transform:uppercase}
.cost{font-size:.8rem;color:#9ca3af}ul{list-style:none;font-size:.85rem;margin:6px 0 10px}
li{padding:3px 0;border-bottom:1px dashed #2a3038}.tip{font-size:.85rem;background:#252a32;padding:8px;border-radius:6px}
</style></head><body>
<h1>STALZONE • Справочник Бартера</h1>__DOWNLOAD_BTN__
<div class="factions" id="factions">
<button class="f-btn stalker active" data-f="stalker">🛡 Сталкеры</button>
<button class="f-btn bandit" data-f="bandit">☠️ Бандиты</button></div>
<input id="q" placeholder="Поиск по названию, обвесу или ветке...">
<div class="tabs" id="tabs">
<button class="tab active" data-c="Все">Все</button><button class="tab" data-c="Оружие">Оружие</button>
<button class="tab" data-c="Вторичное">Вторичное</button><button class="tab" data-c="Броня">Броня</button>
<button class="tab" data-c="Контейнеры">Контейнеры</button></div>
<div id="content"></div>
<script>
const D=__DATA__;let fac="stalker",cat="Все",qry="";
function draw(){
const res=D.filter(i=>(i.faction==="all"||i.faction===fac)&&(cat==="Все"||i.category===cat)&&JSON.stringify(i).toLowerCase().includes(qry));
document.getElementById("content").innerHTML=res.map(i=>`<div class="card">
<div class="title">${i.name} (${i.category})</div><div class="role">${i.role}</div>
<div class="tree">${i.steps.map(s=>`<div class="step"><div class="st">${s.stage}</div><b>${s.item}</b><div class="cost">${s.cost}</div></div>`).join("")}</div>
<b>Обвесы / Модули:</b><ul>${i.attachments.map(a=>`<li>• ${a}</li>`).join("")}</ul>
<div class="tip">💡 ${i.tip}</div></div>`).join("")||"<p>Ничего не найдено</p>";
}
document.getElementById("factions").onclick=e=>{if(e.target.dataset.f){document.querySelectorAll(".f-btn").forEach(b=>b.classList.remove("active"));e.target.classList.add("active");fac=e.target.dataset.f;draw()}};
document.getElementById("tabs").onclick=e=>{if(e.target.dataset.c){document.querySelectorAll(".tab").forEach(b=>b.classList.remove("active"));e.target.classList.add("active");cat=e.target.dataset.c;draw()}};
document.getElementById("q").oninput=e=>{qry=e.target.value.toLowerCase();draw()};draw();
</script></body></html>"""

data_json = json.dumps(BARTER_DATA, ensure_ascii=False)
dl_html = '<div class="dl-box"><a class="dl-btn" href="stalzone_offline.html" download="STALZONE_Barter_Offline.html">📥 Скачать офлайн-версию</a></div>'

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML.replace("__DATA__", data_json).replace("__DOWNLOAD_BTN__", dl_html))

with open("stalzone_offline.html", "w", encoding="utf-8") as f:
    f.write(HTML.replace("__DATA__", data_json).replace("__DOWNLOAD_BTN__", ""))

print("Готово! Созданы файлы index.html и stalzone_offline.html для GitHub.")