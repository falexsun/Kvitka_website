import os

top = open('top.txt').read()
bottom = open('bottom.txt').read()

# Add hidden developer credit to bottom
bottom = bottom.replace('</footer>', '''
  <!-- Блок Разработчика (Скрыт до релиза) -->
  <!--
  <div class="developer-credit" style="margin-top: 32px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 12px; color: rgba(255,255,255,0.4); font-weight: 500; letter-spacing: 0.05em; font-family: var(--sans);">
    Система и дизайн — <a href="https://yourwebsite.ru" target="_blank" style="color: rgba(255,255,255,0.6); transition: color 0.3s; text-decoration: none; font-weight: 600;" onmouseover="this.style.color=\'var(--blue-soft)\'" onmouseout="this.style.color=\'rgba(255,255,255,0.6)\'">Имя Разработчика</a>
  </div>
  -->
</footer>
''')

bio_content = top + '''
<style>
/* EXTRA STYLES FOR INNER PAGES */
.inner-hero { padding: 140px 6vw 60px; background: var(--off); position: relative; overflow: hidden; }
.inner-hero::before { content: ''; position: absolute; right: -10vw; top: -20vh; width: 40vw; height: 40vw; background: var(--blue-soft); border-radius: 50%; filter: blur(100px); opacity: 0.5; z-index: 0; }
.inner-hero::after { content: ''; position: absolute; left: -10vw; bottom: -20vh; width: 30vw; height: 30vw; background: var(--red-pale); border-radius: 50%; filter: blur(80px); opacity: 0.2; z-index: 0; }
.breadcrumbs { position: relative; z-index: 1; display: flex; gap: 8px; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 24px; font-weight: 600; }
.breadcrumbs a { color: var(--blue); transition: color 0.3s; }
.breadcrumbs a:hover { color: var(--navy); }
.inner-title { position: relative; z-index: 1; font-family: var(--serif); font-size: clamp(36px, 5vw, 64px); font-weight: 700; color: var(--navy); line-height: 1.1; margin-bottom: 20px; letter-spacing: -0.01em; }

/* BIOGRAPHY GRID */
.bio-page { padding: 80px 6vw; display: grid; grid-template-columns: 1fr 340px; gap: 60px; align-items: start; position: relative; overflow: hidden; }
.bio-page::after { content: 'ЕДИНАЯ РОССИЯ'; position: absolute; left: -5vw; top: 40vh; transform: rotate(-90deg); font-family: var(--sans); font-size: 14vw; font-weight: 800; color: rgba(0,64,128,0.02); pointer-events: none; white-space: nowrap; z-index: 0; letter-spacing: 0.05em; }

.bio-main { font-size: 18px; line-height: 1.8; color: var(--text); position: relative; z-index: 2; }
.bio-main p { margin-bottom: 24px; }
.bio-main h3 { font-family: var(--serif); font-size: 32px; color: var(--navy); margin: 56px 0 24px; font-weight: 700; }
.bio-sidebar { position: sticky; top: 100px; z-index: 2; }
.bio-photo-card { background: var(--white); box-shadow: var(--shadow-md); border-radius: 4px; overflow: hidden; margin-bottom: 32px; border: 1px solid var(--border); }
.bio-photo-wrap { aspect-ratio: 3/4; background: var(--off); position: relative; }
.bio-params { padding: 24px; }
.bio-param { margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
.bio-param:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
.bp-label { font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted); margin-bottom: 4px; font-weight: 600; }
.bp-val { font-size: 14px; font-weight: 600; color: var(--navy); }
.er-emblem { text-align: center; margin-top: 40px; opacity: 0.8; filter: grayscale(10%); transition: all 0.3s; }
.er-emblem:hover { opacity: 1; filter: grayscale(0%); transform: scale(1.05); }
.er-emblem img { width: 120px; margin: 0 auto; }
@media(max-width: 900px) { .bio-page { grid-template-columns: 1fr; } .bio-sidebar { position: static; order: -1; } .bio-page::after { display: none; } }
</style>

<div class="inner-hero">
  <div class="breadcrumbs rv"><a href="kvitka-light.html">Главная</a> <span>/</span> <span>Биография</span></div>
  <h1 class="inner-title rv">Квитка Иван Иванович</h1>
</div>

<section class="bio-page">
  <div class="bio-main rv">
    <p>Родился в городе Тюмени. Доктор социологических наук. Вся профессиональная деятельность неразрывно связана с Тюменской областью и служением интересам граждан на государственном уровне.</p>
    <p>Является действующим депутатом Государственной Думы Федерального Собрания Российской Федерации от Тюменской области, где представляет интересы избирателей и работает над законодательным укреплением страны.</p>
    
    <h3>Образование и наука</h3>
    <p>Имеет блестящее высшее образование и академический опыт. В своей работе опирается на значительную научную базу, опыт руководителя и глубокое понимание социальной структуры общества и региональной специфики.</p>
    <p>Много лет посвятил исследованию социологических процессов региона, автор научных работ, посвященных развитию гражданского общества и совершенствованию механизмов взаимодействия власти и народа.</p>

    <h3>Партийная и законодательная работа</h3>
    <p>Член фракции Политической партии <strong>«ЕДИНАЯ РОССИЯ»</strong> в Государственной Думе. Входит в состав руководящих органов партии. Активно участвует в реализации федеральных партийных проектов и инициатив на территории региона.</p>
    <p>В рамках законотворческой деятельности выступал инициатором и соавтором ряда социально значимых законопроектов, направленных на:</p>
    <ul style="margin-left:24px; margin-bottom:24px; color:var(--muted)">
      <li>Поддержку социально уязвимых категорий граждан и многодетных семей;</li>
      <li>Развитие российской экономики и региональной инфраструктуры;</li>
      <li>Укрепление суверенитета и безопасности Российской Федерации.</li>
    </ul>

    <h3>Общественная позиция</h3>
    <p style="font-family: var(--serif); font-size: 24px; font-style: italic; color: var(--navy); border-left: 3px solid var(--blue); padding-left: 24px; margin: 40px 0;">«Моя главная задача — слышать людей и решать их проблемы. Только через постоянный диалог мы можем создавать законы, которые работают на благо нашей великой страны — России».</p>
  </div>
  
  <aside class="bio-sidebar rv">
    <div class="bio-photo-card">
      <div class="bio-photo-wrap">
        <div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:var(--serif); font-size:90px; opacity:0.05; color:var(--navy);">ИК</div>
        <!-- Decoration flag line at bottom of photo -->
        <div style="position:absolute; bottom:0; left:0; right:0; height:6px; background:linear-gradient(90deg, var(--white), var(--blue), var(--red));"></div>
      </div>
      <div class="bio-params">
        <div class="bio-param">
          <div class="bp-label">Должность</div>
          <div class="bp-val">Депутат Государственной Думы РФ</div>
        </div>
        <div class="bio-param">
          <div class="bp-label">Фракция</div>
          <div class="bp-val">«ЕДИНАЯ РОССИЯ»</div>
        </div>
        <div class="bio-param">
          <div class="bp-label">Регион</div>
          <div class="bp-val">Тюменская область</div>
        </div>
        <div class="bio-param">
          <div class="bp-label">Созыв</div>
          <div class="bp-val">VIII созыв</div>
        </div>
      </div>
    </div>
    
    <div class="er-emblem">
      <div style="font-size: 72px; margin-bottom: 8px; line-height: 1;">🐻</div>
      <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 800; color: var(--navy);">Партия<br><span style="color: var(--blue)">Единая Россия</span></div>
    </div>
  </aside>
</section>
''' + bottom


albums_content = top + '''
<style>
/* EXTRA STYLES FOR INNER PAGES */
.inner-hero { padding: 140px 6vw 60px; background: var(--off); position: relative; overflow: hidden; }
.inner-hero::before { content: ''; position: absolute; right: -10vw; top: -20vh; width: 40vw; height: 40vw; background: var(--blue-soft); border-radius: 50%; filter: blur(100px); opacity: 0.5; z-index: 0; }
.breadcrumbs { position: relative; z-index: 1; display: flex; gap: 8px; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 24px; font-weight: 600; }
.breadcrumbs a { color: var(--blue); transition: color 0.3s; }
.breadcrumbs a:hover { color: var(--navy); }
.inner-title { position: relative; z-index: 1; font-family: var(--serif); font-size: clamp(36px, 5vw, 64px); font-weight: 700; color: var(--navy); line-height: 1.1; margin-bottom: 20px; letter-spacing: -0.01em; }

/* ALBUMS GRID */
.albums-page { padding: 80px 6vw 120px; background: var(--white); position: relative; }
.albums-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 40px; position: relative; z-index: 2; }
.album-card { display: block; border: 1px solid var(--border); border-radius: 4px; overflow: hidden; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); background: var(--white); }
.album-card:hover { transform: translateY(-8px); box-shadow: var(--shadow-lg); border-color: rgba(0,64,128,0.15); }
.album-img { aspect-ratio: 16/10; background: var(--off); position: relative; overflow: hidden; }
.album-img::after { content: ''; position: absolute; inset: 0; background: linear-gradient(0deg, rgba(11,22,44,0.8) 0%, transparent 60%); opacity: 0.6; transition: opacity 0.4s; }
.album-card:hover .album-img::after { opacity: 0.9; }
.album-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1); }
.album-card:hover .album-img img { transform: scale(1.05); }
.album-count { position: absolute; top: 16px; right: 16px; background: rgba(255,255,255,0.95); backdrop-filter: blur(8px); padding: 8px 16px; border-radius: 2px; font-size: 10px; font-weight: 700; letter-spacing: 0.15em; color: var(--navy); z-index: 2; box-shadow: 0 4px 16px rgba(0,0,0,0.1); }
.album-info { padding: 28px; position: relative; }
.album-info::before { content:''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--white), var(--blue), var(--red)); transform: scaleX(0); transform-origin: left; transition: transform 0.4s ease; }
.album-card:hover .album-info::before { transform: scaleX(1); }
.album-date { font-size: 11px; font-weight: 700; letter-spacing: 0.15em; color: var(--blue); margin-bottom: 12px; text-transform: uppercase; }
.album-title { font-family: var(--serif); font-size: 24px; font-weight: 700; color: var(--navy); line-height: 1.3; margin-bottom: 12px; }
.album-desc { font-size: 14px; color: var(--muted); line-height: 1.6; }

/* DECORATION */
.rus-decor { position: fixed; bottom: -10vh; right: -10vw; font-family: var(--sans); font-size: 40vw; font-weight: 900; color: rgba(0,64,128,0.02); pointer-events: none; z-index: 0; letter-spacing: -0.05em; line-height: 0.8; }
</style>

<div class="inner-hero">
  <div class="breadcrumbs rv"><a href="kvitka-light.html">Главная</a> <span>/</span> <span>Пресс-центр</span></div>
  <h1 class="inner-title rv">Фотоархив событий</h1>
</div>

<section class="albums-page rv">
  <!-- Russia subtle text background -->
  <div class="rus-decor">РФ</div>

  <div class="albums-grid">
    <!-- Album 1 -->
    <a href="#" class="album-card rv">
      <div class="album-img">
        <div class="album-count">24 ФОТО</div>
        <!-- <img src="path" alt=""> -->
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:56px;color:rgba(255,255,255,0.7);z-index:1;">📷</div>
      </div>
      <div class="album-info">
        <div class="album-date">12 МАЯ 2026</div>
        <h3 class="album-title">Встреча с избирателями в Тюмени</h3>
        <p class="album-desc">Обсуждение вопросов благоустройства и социальной поддержки жителей региона.</p>
      </div>
    </a>
    
    <!-- Album 2 -->
    <a href="#" class="album-card rv">
      <div class="album-img">
        <div class="album-count">18 ФОТО</div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:56px;color:rgba(255,255,255,0.7);z-index:1;">🇷🇺</div>
      </div>
      <div class="album-info">
        <div class="album-date">09 МАЯ 2026</div>
        <h3 class="album-title">Празднование Дня Победы</h3>
        <p class="album-desc">Участие в торжественном параде и возложение цветов к мемориалу памяти.</p>
      </div>
    </a>

    <!-- Album 3 -->
    <a href="#" class="album-card rv">
      <div class="album-img">
        <div class="album-count">32 ФОТО</div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:56px;color:rgba(255,255,255,0.7);z-index:1;">🏛️</div>
      </div>
      <div class="album-info">
        <div class="album-date">28 АПР 2026</div>
        <h3 class="album-title">Пленарное заседание ГД ФС РФ</h3>
        <p class="album-desc">Выступление по вопросам бюджета и регионального инфраструктурного развития.</p>
      </div>
    </a>

    <!-- Album 4 -->
    <a href="#" class="album-card rv">
      <div class="album-img">
        <div class="album-count">15 ФОТО</div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:56px;color:rgba(255,255,255,0.7);z-index:1;">🗳️</div>
      </div>
      <div class="album-info">
        <div class="album-date">15 МАР 2026</div>
        <h3 class="album-title">Съезд партии «Единая Россия»</h3>
        <p class="album-desc">Участие в работе центральных органов партии и обсуждение региональных проектов.</p>
      </div>
    </a>
    
    <!-- Album 5 -->
    <a href="#" class="album-card rv">
      <div class="album-img">
        <div class="album-count">21 ФОТО</div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:56px;color:rgba(255,255,255,0.7);z-index:1;">🎓</div>
      </div>
      <div class="album-info">
        <div class="album-date">01 СЕН 2025</div>
        <h3 class="album-title">Открытие новой школы</h3>
        <p class="album-desc">Рабочий визит на объект социальной инфраструктуры, построенный по партийному проекту.</p>
      </div>
    </a>

    <!-- Album 6 -->
    <a href="#" class="album-card rv">
      <div class="album-img">
        <div class="album-count">44 ФОТО</div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:56px;color:rgba(255,255,255,0.7);z-index:1;">🤝</div>
      </div>
      <div class="album-info">
        <div class="album-date">10 АВГ 2025</div>
        <h3 class="album-title">Прием граждан по личным вопросам</h3>
        <p class="album-desc">Региональная неделя в Тюменской области, решения обращений и инициатив жителей.</p>
      </div>
    </a>
  </div>
</section>
''' + bottom

with open('biography.html', 'w') as f:
    f.write(bio_content)

with open('albums.html', 'w') as f:
    f.write(albums_content)

# Update main file's developer credit as well
main_content = open('kvitka-light.html').read()
new_main = main_content.replace('</footer>', '''
  <!-- Блок Разработчика (Скрыт до релиза) -->
  <!--
  <div class="developer-credit" style="margin-top: 32px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 12px; color: rgba(255,255,255,0.4); font-weight: 500; letter-spacing: 0.05em; font-family: var(--sans);">
    Система и дизайн — <a href="https://yourwebsite.ru" target="_blank" style="color: rgba(255,255,255,0.6); transition: color 0.3s; text-decoration: none; font-weight: 600;" onmouseover="this.style.color=\'var(--blue-soft)\'" onmouseout="this.style.color=\'rgba(255,255,255,0.6)\'">Имя Разработчика</a>
  </div>
  -->
</footer>
''')
# Update links
new_main = new_main.replace('<a href="#" class="btn-main">Полная биография →</a>', '<a href="biography.html" class="btn-main">Полная биография →</a>')
new_main = new_main.replace('<a href="#" class="sec-link">Весь архив →</a>', '<a href="albums.html" class="sec-link">Весь архив →</a>')

with open('kvitka-light.html', 'w') as f:
    f.write(new_main)
