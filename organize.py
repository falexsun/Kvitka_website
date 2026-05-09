import os
import re

os.makedirs('news', exist_ok=True)

# Read top and bottom parts from our index
with open('kvitka-light.html', 'r') as f:
    main_content = f.read()

top = main_content.split('<!-- HERO -->')[0]
bottom = '<footer' + main_content.split('<footer')[1]

# Make links relative to parent
def make_relative(html_str):
    html_str = html_str.replace('href="#', 'href="../kvitka-light.html#')
    html_str = html_str.replace('href="biography.html"', 'href="../biography.html"')
    html_str = html_str.replace('href="albums.html"', 'href="../albums.html"')
    # If it was already pointing to kvitka-light.html in top/bottom
    html_str = html_str.replace('href="kvitka-light.html', 'href="../kvitka-light.html')
    return html_str

top = make_relative(top)
bottom = make_relative(bottom)

event_content = top + '''
<style>
/* EXTRA STYLES FOR EVENT PAGE */
.inner-hero { padding: 140px 6vw 60px; background: var(--off); position: relative; overflow: hidden; }
.breadcrumbs { position: relative; z-index: 1; display: flex; gap: 8px; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 24px; font-weight: 600; flex-wrap: wrap; }
.breadcrumbs a { color: var(--blue); transition: color 0.3s; }
.breadcrumbs a:hover { color: var(--navy); }
.event-tag { display: inline-block; padding: 4px 10px; background: rgba(0,64,128,0.1); color: var(--blue); font-size: 10px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; border-radius: 2px; margin-bottom: 16px; }
.inner-title { position: relative; z-index: 1; font-family: var(--serif); font-size: clamp(32px, 5vw, 56px); font-weight: 700; color: var(--navy); line-height: 1.2; margin-bottom: 20px; letter-spacing: -0.01em; max-width: 900px; }
.event-meta { display: flex; gap: 24px; font-size: 12px; color: var(--muted); font-weight: 600; }
.event-meta span { display: flex; align-items: center; gap: 6px; }

/* EVENT CONTENT */
.event-page { padding: 60px 6vw 120px; background: var(--white); }
.event-main-img { width: 100%; max-width: 1000px; aspect-ratio: 16/9; background: var(--off); border-radius: 4px; overflow: hidden; margin-bottom: 48px; position: relative; }
.event-main-img img { width: 100%; height: 100%; object-fit: cover; }
.event-content-wrap { display: grid; grid-template-columns: 1fr 340px; gap: 60px; max-width: 1200px; }
.event-text { font-size: 17px; line-height: 1.8; color: var(--text); }
.event-text p { margin-bottom: 24px; }
.event-text h2 { font-family: var(--serif); font-size: 28px; color: var(--navy); margin: 48px 0 20px; }
.event-text blockquote { font-family: var(--serif); font-size: 24px; font-style: italic; color: var(--navy); border-left: 3px solid var(--blue); padding-left: 24px; margin: 40px 0; }
.event-gallery { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 40px 0; }
.event-gallery-item { aspect-ratio: 4/3; background: var(--off); border-radius: 2px; display: flex; align-items: center; justify-content: center; font-size: 32px; color: rgba(0,0,0,0.1); }

/* SIDEBAR */
.sidebar-widget { background: var(--off); padding: 32px; border-radius: 4px; border: 1px solid var(--border); margin-bottom: 32px; }
.widget-title { font-size: 11px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--blue); margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 12px; }
.recent-list { list-style: none; }
.recent-list li { margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
.recent-list li:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
.recent-list a { display: block; font-size: 14px; font-weight: 600; color: var(--navy); line-height: 1.4; margin-bottom: 6px; transition: color 0.3s; }
.recent-list a:hover { color: var(--blue); }
.recent-date { font-size: 11px; color: var(--muted); }

@media(max-width: 900px) { .event-content-wrap { grid-template-columns: 1fr; } }
</style>

<div class="inner-hero">
  <div class="breadcrumbs rv"><a href="../kvitka-light.html">Главная</a> <span>/</span> <a href="../kvitka-light.html#news">Новости</a> <span>/</span> <span>Событие</span></div>
  <div class="event-tag rv">Прием граждан</div>
  <h1 class="inner-title rv">В Тюмени прошел личный прием граждан: решены вопросы благоустройства и социальной поддержки</h1>
  <div class="event-meta rv">
    <span>Опубликовано: 12 МАЯ 2026</span>
    <span>👁️ 342 просмотра</span>
  </div>
</div>

<section class="event-page rv">
  <div class="event-main-img">
    <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:64px;background:#f0f4f8;color:rgba(0,64,128,0.1);">📸 Главное фото события</div>
  </div>

  <div class="event-content-wrap">
    <div class="event-text">
      <p>В рамках региональной недели депутат Государственной Думы Иван Квитка провел личный прием жителей Тюменской области. Вопросы, с которыми обратились граждане, касались самых разных сфер жизни: от благоустройства дворовых территорий до обеспечения льготными лекарствами.</p>
      
      <h2>Реальные дела и решения</h2>
      <p>Ключевой темой обсуждения стали вопросы жилищно-коммунального хозяйства и ремонта инфраструктурных объектов в муниципальных районах области. По итогам встречи были направлены официальные депутатские запросы в профильные департаменты регионального Правительства.</p>
      
      <blockquote>«Каждое обращение — это чья-то судьба и конкретная проблема, которая требует немедленного включения. Для нас нет мелких вопросов, когда речь идет о качестве жизни наших граждан».</blockquote>
      
      <p>Особое внимание было уделено обращениям многодетных семей и семей участников специальной военной операции. Депутат подчеркнул важность неукоснительного соблюдения всех федеральных и региональных мер поддержки.</p>

      <div class="event-gallery">
        <div class="event-gallery-item">📷</div>
        <div class="event-gallery-item">🤝</div>
      </div>

      <p>В завершение приема Иван Квитка отметил высокую гражданскую активность жителей Тюменской области. Практика проведения регулярных встреч с населением будет продолжена, все поступившие обращения взяты на личный депутатский контроль до полного их решения.</p>
      
      <div style="margin-top: 48px;">
        <a href="../kvitka-light.html#news" class="btn-hero-sec" style="color: var(--navy); border-color: var(--border);">← Вернуться к новостям</a>
      </div>
    </div>
    
    <aside class="event-sidebar">
      <div class="sidebar-widget">
        <div class="widget-title">Читайте также</div>
        <ul class="recent-list">
          <li>
            <a href="12346.html">Участие в пленарном заседании ГД ФС РФ по вопросам бюджета</a>
            <div class="recent-date">05 МАЯ 2026</div>
          </li>
          <li>
            <a href="12347.html">Поздравление ветеранов с Днем Великой Победы</a>
            <div class="recent-date">09 МАЯ 2026</div>
          </li>
        </ul>
      </div>
      <div class="sidebar-widget" style="text-align: center; padding: 40px 24px;">
        <div style="font-size: 48px; margin-bottom: 16px;">✉️</div>
        <h4 style="font-size: 16px; color: var(--navy); margin-bottom: 12px; font-weight: 700;">Есть предложение?</h4>
        <p style="font-size: 12px; color: var(--muted); margin-bottom: 20px;">Направьте официальное обращение депутату онлайн</p>
        <a href="../kvitka-light.html#contact" class="btn-hero-main" style="width: 100%; justify-content: center; padding: 12px;">Написать</a>
      </div>
    </aside>
  </div>
</section>
''' + bottom

with open('news/12345.html', 'w') as f:
    f.write(event_content)

# Update links in main file
main_content = main_content.replace('href="event.html"', 'href="news/12345.html"')
main_content = re.sub(r'class="n-card(.*?)href="[^"]*"', r'class="n-card\1href="news/12345.html"', main_content)

with open('kvitka-light.html', 'w') as f:
    f.write(main_content)

# Do the same for albums
if os.path.exists('albums.html'):
    with open('albums.html', 'r') as f:
        alb_content = f.read()
    alb_content = re.sub(r'class="album-card(.*?)href="[^"]*"', r'class="album-card\1href="news/12345.html"', alb_content)
    with open('albums.html', 'w') as f:
        f.write(alb_content)
        
if os.path.exists('event.html'):
    os.remove('event.html')

print("DONE URL REORGANIZATION")