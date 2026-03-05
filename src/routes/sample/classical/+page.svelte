<script lang="ts">
	import { featuredPoems, bioText, categories } from '$lib/utils/poems';

	let scrollY = $state(0);
</script>

<svelte:window bind:scrollY={scrollY} />

<svelte:head>
	<title>سمير الشيخ - ديوان شعر</title>
	<meta name="description" content="ديوان الشاعر سمير الشيخ - مجموعة من روائع القصائد العربية الفصيحة" />
</svelte:head>

<!-- Navigation -->
<nav class="nav" class:nav--scrolled={scrollY > 50}>
	<div class="nav__inner">
		<a href="#hero" class="nav__logo">سمير الشيخ</a>
		<ul class="nav__links">
			<li><a href="#hero" class="nav__link nav__link--active">الرئيسية</a></li>
			<li><a href="#poems" class="nav__link">الديوان</a></li>
			<li><a href="#about" class="nav__link">عن الشاعر</a></li>
			<li><a href="#footer" class="nav__link">تواصل</a></li>
		</ul>
	</div>
</nav>

<!-- Hero Section -->
<section id="hero" class="hero">
	<div class="hero__content">
		<!-- Geometric border top -->
		<svg class="geo-border" viewBox="0 0 800 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
			<defs>
				<pattern id="star-pattern" x="0" y="0" width="60" height="60" patternUnits="userSpaceOnUse">
					<path d="M30 5 L35 20 L50 20 L38 30 L42 45 L30 36 L18 45 L22 30 L10 20 L25 20 Z" fill="none" stroke="#B8860B" stroke-width="1"/>
					<circle cx="30" cy="30" r="3" fill="#B8860B" opacity="0.4"/>
					<rect x="0" y="0" width="60" height="60" fill="none" stroke="#B8860B" stroke-width="0.5" opacity="0.3"/>
				</pattern>
			</defs>
			<rect width="800" height="60" fill="url(#star-pattern)"/>
			<line x1="0" y1="0" x2="800" y2="0" stroke="#B8860B" stroke-width="2"/>
			<line x1="0" y1="59" x2="800" y2="59" stroke="#B8860B" stroke-width="2"/>
		</svg>

		<h1 class="hero__name">سمير الشيخ</h1>
		<p class="hero__subtitle">ديوان شعر</p>

		{#if featuredPoems[0]}
			<div class="hero__verse">
				<span class="hero__verse-sadr">{featuredPoems[0].verses[0].sadr}</span>
				<span class="hero__verse-divider"></span>
				<span class="hero__verse-ajz">{featuredPoems[0].verses[0].ajz}</span>
			</div>
		{/if}

		<!-- Decorative divider -->
		<svg class="divider-ornament" viewBox="0 0 400 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
			<line x1="0" y1="20" x2="150" y2="20" stroke="#B8860B" stroke-width="1"/>
			<circle cx="160" cy="20" r="3" fill="#B8860B"/>
			<path d="M175 10 Q200 0 225 10 Q200 20 175 10 Z" fill="#B8860B" opacity="0.6"/>
			<path d="M175 30 Q200 40 225 30 Q200 20 175 30 Z" fill="#B8860B" opacity="0.6"/>
			<circle cx="200" cy="20" r="5" fill="none" stroke="#B8860B" stroke-width="1.5"/>
			<circle cx="200" cy="20" r="2" fill="#B8860B"/>
			<circle cx="240" cy="20" r="3" fill="#B8860B"/>
			<line x1="250" y1="20" x2="400" y2="20" stroke="#B8860B" stroke-width="1"/>
		</svg>

		<a href="#poems" class="hero__cta">استكشف الديوان</a>
	</div>
</section>

<!-- Featured Poems Section -->
<section id="poems" class="poems">
	<div class="poems__header">
		<svg class="section-divider" viewBox="0 0 600 30" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
			<line x1="0" y1="15" x2="200" y2="15" stroke="#B8860B" stroke-width="1"/>
			<polygon points="210,5 220,15 210,25 200,15" fill="#B8860B" opacity="0.5"/>
			<polygon points="230,5 240,15 230,25 220,15" fill="none" stroke="#B8860B" stroke-width="1"/>
			<rect x="245" y="10" width="10" height="10" fill="none" stroke="#B8860B" stroke-width="1" transform="rotate(45 250 15)"/>
			<rect x="265" y="10" width="10" height="10" fill="none" stroke="#B8860B" stroke-width="1" transform="rotate(45 270 15)"/>
			<polygon points="290,5 300,15 290,25 280,15" fill="none" stroke="#B8860B" stroke-width="1"/>
			<polygon points="310,5 320,15 310,25 300,15" fill="#B8860B" opacity="0.5"/>
			<line x1="320" y1="15" x2="600" y2="15" stroke="#B8860B" stroke-width="1"/>
		</svg>
		<h2 class="poems__title">من روائع القصائد</h2>
		<svg class="section-divider" viewBox="0 0 600 30" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
			<line x1="0" y1="15" x2="200" y2="15" stroke="#B8860B" stroke-width="1"/>
			<polygon points="210,5 220,15 210,25 200,15" fill="#B8860B" opacity="0.5"/>
			<polygon points="230,5 240,15 230,25 220,15" fill="none" stroke="#B8860B" stroke-width="1"/>
			<rect x="245" y="10" width="10" height="10" fill="none" stroke="#B8860B" stroke-width="1" transform="rotate(45 250 15)"/>
			<rect x="265" y="10" width="10" height="10" fill="none" stroke="#B8860B" stroke-width="1" transform="rotate(45 270 15)"/>
			<polygon points="290,5 300,15 290,25 280,15" fill="none" stroke="#B8860B" stroke-width="1"/>
			<polygon points="310,5 320,15 310,25 300,15" fill="#B8860B" opacity="0.5"/>
			<line x1="320" y1="15" x2="600" y2="15" stroke="#B8860B" stroke-width="1"/>
		</svg>
	</div>

	<div class="poems__grid">
		{#each featuredPoems as poem}
			<article class="poem-card">
				<!-- Corner arabesques -->
				<svg class="poem-card__corner poem-card__corner--top-right" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
					<path d="M0 0 Q20 0 20 20 Q20 0 40 0" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<path d="M0 0 Q0 20 20 20 Q0 20 0 40" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<circle cx="10" cy="10" r="2" fill="#B8860B" opacity="0.5"/>
				</svg>
				<svg class="poem-card__corner poem-card__corner--top-left" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
					<path d="M0 0 Q20 0 20 20 Q20 0 40 0" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<path d="M40 0 Q40 20 20 20 Q40 20 40 40" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<circle cx="30" cy="10" r="2" fill="#B8860B" opacity="0.5"/>
				</svg>
				<svg class="poem-card__corner poem-card__corner--bottom-right" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
					<path d="M0 40 Q20 40 20 20 Q20 40 40 40" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<path d="M0 40 Q0 20 20 20 Q0 20 0 0" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<circle cx="10" cy="30" r="2" fill="#B8860B" opacity="0.5"/>
				</svg>
				<svg class="poem-card__corner poem-card__corner--bottom-left" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
					<path d="M0 40 Q20 40 20 20 Q20 40 40 40" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<path d="M40 40 Q40 20 20 20 Q40 20 40 0" fill="none" stroke="#B8860B" stroke-width="1.5"/>
					<circle cx="30" cy="30" r="2" fill="#B8860B" opacity="0.5"/>
				</svg>

				<div class="poem-card__top-border"></div>
				<div class="poem-card__body">
					<h3 class="poem-card__title">{poem.title}</h3>
					<span class="poem-card__badge">{categories[poem.category]}</span>

					<div class="poem-card__verses">
						{#each poem.verses.slice(0, 2) as verse}
							<div class="verse-line">
								<span class="verse-line__sadr">{verse.sadr}</span>
								<span class="verse-line__divider"></span>
								<span class="verse-line__ajz">{verse.ajz}</span>
							</div>
						{/each}
					</div>

					<a href="/sample/classical" class="poem-card__link">اقرأ القصيدة</a>
				</div>
			</article>
		{/each}
	</div>
</section>

<!-- Stats Bar -->
<section class="stats">
	<div class="stats__inner">
		<div class="stats__item">
			<span class="stats__number">٣٠٠+</span>
			<span class="stats__label">قصيدة</span>
		</div>
		<div class="stats__separator"></div>
		<div class="stats__item">
			<span class="stats__number">٥٠+</span>
			<span class="stats__label">سنة من الشعر</span>
		</div>
		<div class="stats__separator"></div>
		<div class="stats__item">
			<span class="stats__number">٩</span>
			<span class="stats__label">أبواب شعرية</span>
		</div>
	</div>
</section>

<!-- About Preview -->
<section id="about" class="about">
	<div class="about__inner">
		<div class="about__medallion">
			<!-- Shamsa (sun medallion) SVG -->
			<svg class="shamsa" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
				<defs>
					<clipPath id="shamsa-clip">
						<circle cx="150" cy="150" r="140"/>
					</clipPath>
				</defs>
				<!-- Outer ring -->
				<circle cx="150" cy="150" r="140" fill="none" stroke="#B8860B" stroke-width="2"/>
				<circle cx="150" cy="150" r="135" fill="none" stroke="#B8860B" stroke-width="0.5"/>
				<!-- Radiating petals -->
				{#each Array(16) as _, i}
					<line
						x1="150"
						y1="150"
						x2={150 + 130 * Math.cos((i * 22.5 * Math.PI) / 180)}
						y2={150 + 130 * Math.sin((i * 22.5 * Math.PI) / 180)}
						stroke="#B8860B"
						stroke-width="0.5"
						opacity="0.3"
					/>
				{/each}
				{#each Array(12) as _, i}
					<ellipse
						cx={150 + 90 * Math.cos((i * 30 * Math.PI) / 180)}
						cy={150 + 90 * Math.sin((i * 30 * Math.PI) / 180)}
						rx="18"
						ry="8"
						fill="none"
						stroke="#B8860B"
						stroke-width="1"
						transform="rotate({i * 30} {150 + 90 * Math.cos((i * 30 * Math.PI) / 180)} {150 + 90 * Math.sin((i * 30 * Math.PI) / 180)})"
						opacity="0.6"
					/>
				{/each}
				<!-- Inner decorative rings -->
				<circle cx="150" cy="150" r="60" fill="none" stroke="#B8860B" stroke-width="1.5"/>
				<circle cx="150" cy="150" r="55" fill="none" stroke="#B8860B" stroke-width="0.5"/>
				{#each Array(8) as _, i}
					<path
						d="M150,90 Q{150 + 25 * Math.cos(((i * 45 - 22.5) * Math.PI) / 180)},{150 + 25 * Math.sin(((i * 45 - 22.5) * Math.PI) / 180)} {150 + 60 * Math.cos((i * 45 * Math.PI) / 180)},{150 + 60 * Math.sin((i * 45 * Math.PI) / 180)}"
						fill="none"
						stroke="#B8860B"
						stroke-width="1"
						opacity="0.5"
					/>
				{/each}
				<!-- Center ornament -->
				<circle cx="150" cy="150" r="25" fill="none" stroke="#B8860B" stroke-width="2"/>
				<circle cx="150" cy="150" r="20" fill="none" stroke="#B8860B" stroke-width="0.5"/>
				<circle cx="150" cy="150" r="8" fill="#B8860B" opacity="0.3"/>
				<circle cx="150" cy="150" r="3" fill="#B8860B"/>
				<!-- Outer petal tips -->
				{#each Array(24) as _, i}
					<circle
						cx={150 + 125 * Math.cos((i * 15 * Math.PI) / 180)}
						cy={150 + 125 * Math.sin((i * 15 * Math.PI) / 180)}
						r="2"
						fill="#B8860B"
						opacity="0.4"
					/>
				{/each}
			</svg>
		</div>
		<div class="about__text">
			<h2 class="about__title">عن الشاعر</h2>
			<p class="about__bio">{bioText}</p>
		</div>
	</div>
</section>

<!-- Footer -->
<footer id="footer" class="footer">
	<div class="footer__inner">
		<!-- Decorative motif -->
		<svg class="footer__motif" viewBox="0 0 100 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
			<path d="M10 20 Q25 5 50 20 Q75 35 90 20" fill="none" stroke="#B8860B" stroke-width="1"/>
			<path d="M10 20 Q25 35 50 20 Q75 5 90 20" fill="none" stroke="#B8860B" stroke-width="1"/>
			<circle cx="50" cy="20" r="4" fill="none" stroke="#B8860B" stroke-width="1"/>
			<circle cx="50" cy="20" r="1.5" fill="#B8860B"/>
			<circle cx="10" cy="20" r="2" fill="#B8860B" opacity="0.5"/>
			<circle cx="90" cy="20" r="2" fill="#B8860B" opacity="0.5"/>
		</svg>

		<p class="footer__name">سمير الشيخ</p>
		<p class="footer__copy">جميع الحقوق محفوظة &copy; {new Date().getFullYear()}</p>

		<ul class="footer__links">
			<li><a href="#hero">الرئيسية</a></li>
			<li><a href="#poems">الديوان</a></li>
			<li><a href="#about">عن الشاعر</a></li>
			<li><a href="#footer">تواصل</a></li>
		</ul>
	</div>
</footer>

<style>
	/* ========================================
	   BASE & TOKENS
	   ======================================== */
	:root {
		--papyrus: #F5ECD7;
		--ink: #2C1810;
		--gold: #B8860B;
		--gold-light: #D4A843;
		--burgundy: #6B1C23;
		--leather: #1A0F0A;
		--font-heading: 'Aref Ruqaa', serif;
		--font-body: 'Amiri', serif;
		--font-ui: 'Noto Naskh Arabic', serif;
	}

	/* Paper grain texture */
	:global(body) {
		margin: 0;
		padding: 0;
	}

	/* ========================================
	   NAVIGATION
	   ======================================== */
	.nav {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 100;
		padding: 0.75rem 1.5rem;
		transition: background-color 0.3s ease, box-shadow 0.3s ease;
		background-color: transparent;
	}

	.nav--scrolled {
		background-color: rgba(245, 236, 215, 0.95);
		box-shadow: 0 2px 20px rgba(44, 24, 16, 0.1);
		backdrop-filter: blur(8px);
	}

	.nav__inner {
		max-width: 1200px;
		margin: 0 auto;
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.nav__logo {
		font-family: var(--font-heading);
		font-size: 1.5rem;
		font-weight: 700;
		color: var(--ink);
		text-decoration: none;
		min-height: 44px;
		display: flex;
		align-items: center;
	}

	.nav__links {
		list-style: none;
		margin: 0;
		padding: 0;
		display: flex;
		gap: 2rem;
	}

	.nav__link {
		font-family: var(--font-ui);
		font-size: 1rem;
		color: var(--ink);
		text-decoration: none;
		min-height: 44px;
		min-width: 44px;
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
		transition: color 0.2s ease;
	}

	.nav__link::after {
		content: '';
		position: absolute;
		bottom: 6px;
		right: 0;
		left: 0;
		height: 2px;
		background-color: var(--gold);
		transform: scaleX(0);
		transition: transform 0.2s ease;
		transform-origin: center;
	}

	.nav__link:hover::after,
	.nav__link--active::after {
		transform: scaleX(1);
	}

	.nav__link:hover {
		color: var(--burgundy);
	}

	/* ========================================
	   HERO
	   ======================================== */
	.hero {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: var(--papyrus);
		background-image:
			repeating-linear-gradient(
				0deg,
				transparent,
				transparent 2px,
				rgba(44, 24, 16, 0.015) 2px,
				rgba(44, 24, 16, 0.015) 4px
			),
			repeating-linear-gradient(
				90deg,
				transparent,
				transparent 2px,
				rgba(44, 24, 16, 0.01) 2px,
				rgba(44, 24, 16, 0.01) 4px
			),
			radial-gradient(ellipse at 20% 50%, rgba(184, 134, 11, 0.05) 0%, transparent 50%),
			radial-gradient(ellipse at 80% 50%, rgba(107, 28, 35, 0.03) 0%, transparent 50%);
		position: relative;
		padding: 2rem;
	}

	.hero__content {
		text-align: center;
		max-width: 800px;
		width: 100%;
	}

	.geo-border {
		width: 100%;
		max-width: 600px;
		height: auto;
		margin: 0 auto 3rem;
		display: block;
		opacity: 0.7;
	}

	.hero__name {
		font-family: var(--font-heading);
		font-size: clamp(3rem, 8vw, 5rem);
		font-weight: 700;
		color: var(--ink);
		margin: 0 0 0.5rem;
		line-height: 1.3;
	}

	.hero__subtitle {
		font-family: var(--font-ui);
		font-size: clamp(1.2rem, 3vw, 1.6rem);
		color: var(--burgundy);
		margin: 0 0 2.5rem;
		letter-spacing: 0.1em;
	}

	.hero__verse {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 1.5rem;
		margin-bottom: 2.5rem;
		font-family: var(--font-body);
		font-size: clamp(1rem, 2.5vw, 1.35rem);
		line-height: 2.2;
		color: var(--ink);
		flex-wrap: wrap;
	}

	.hero__verse-sadr,
	.hero__verse-ajz {
		flex: 1;
		min-width: 200px;
	}

	.hero__verse-sadr {
		text-align: left;
	}

	.hero__verse-ajz {
		text-align: right;
	}

	.hero__verse-divider {
		width: 2px;
		height: 2rem;
		background-color: var(--gold);
		flex-shrink: 0;
	}

	.divider-ornament {
		width: 300px;
		max-width: 80%;
		height: auto;
		margin: 0 auto 2.5rem;
		display: block;
	}

	.hero__cta {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-height: 44px;
		padding: 0.75rem 2.5rem;
		font-family: var(--font-ui);
		font-size: 1.1rem;
		color: var(--gold);
		background: transparent;
		border: 2px solid var(--gold);
		text-decoration: none;
		transition: background-color 0.2s ease, color 0.2s ease;
		cursor: pointer;
	}

	.hero__cta:hover {
		background-color: var(--gold);
		color: var(--papyrus);
	}

	/* ========================================
	   POEMS SECTION
	   ======================================== */
	.poems {
		padding: 5rem 2rem;
		background-color: var(--papyrus);
		background-image:
			repeating-linear-gradient(
				0deg,
				transparent,
				transparent 2px,
				rgba(44, 24, 16, 0.012) 2px,
				rgba(44, 24, 16, 0.012) 4px
			);
	}

	.poems__header {
		text-align: center;
		margin-bottom: 4rem;
	}

	.poems__title {
		font-family: var(--font-heading);
		font-size: clamp(1.8rem, 4vw, 2.5rem);
		font-weight: 700;
		color: var(--ink);
		margin: 1.5rem 0;
	}

	.section-divider {
		width: 100%;
		max-width: 450px;
		height: auto;
		display: block;
		margin: 0 auto;
		opacity: 0.6;
	}

	.poems__grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
		max-width: 1200px;
		margin: 0 auto;
	}

	/* ========================================
	   POEM CARD
	   ======================================== */
	.poem-card {
		position: relative;
		background-color: rgba(245, 236, 215, 0.6);
		border: 1px solid rgba(184, 134, 11, 0.3);
		box-shadow:
			inset 0 0 0 3px rgba(245, 236, 215, 0.8),
			inset 0 0 0 4px rgba(184, 134, 11, 0.2);
		transition: box-shadow 0.2s ease, transform 0.2s ease;
	}

	.poem-card:hover {
		box-shadow:
			inset 0 0 0 3px rgba(245, 236, 215, 0.8),
			inset 0 0 0 4px rgba(184, 134, 11, 0.4),
			0 8px 30px rgba(44, 24, 16, 0.1);
		transform: translateY(-2px);
	}

	.poem-card__corner {
		position: absolute;
		width: 40px;
		height: 40px;
		opacity: 0.6;
		pointer-events: none;
	}

	.poem-card__corner--top-right {
		top: 4px;
		right: 4px;
	}

	.poem-card__corner--top-left {
		top: 4px;
		left: 4px;
	}

	.poem-card__corner--bottom-right {
		bottom: 4px;
		right: 4px;
	}

	.poem-card__corner--bottom-left {
		bottom: 4px;
		left: 4px;
	}

	.poem-card__top-border {
		height: 4px;
		background: linear-gradient(90deg, transparent, var(--gold), transparent);
	}

	.poem-card__body {
		padding: 2rem 1.5rem 1.5rem;
	}

	.poem-card__title {
		font-family: var(--font-heading);
		font-size: 1.5rem;
		font-weight: 700;
		color: var(--ink);
		margin: 0 0 0.75rem;
	}

	.poem-card__badge {
		display: inline-block;
		font-family: var(--font-ui);
		font-size: 0.8rem;
		color: var(--burgundy);
		border: 1px solid var(--burgundy);
		padding: 0.2rem 0.75rem;
		margin-bottom: 1.25rem;
	}

	.poem-card__verses {
		margin-bottom: 1.5rem;
	}

	.verse-line {
		display: flex;
		align-items: baseline;
		gap: 1rem;
		font-family: var(--font-body);
		font-size: 1.05rem;
		line-height: 2.2;
		color: var(--ink);
		margin-bottom: 0.25rem;
	}

	.verse-line__sadr {
		flex: 1;
		text-align: left;
	}

	.verse-line__divider {
		width: 1px;
		height: 1.2rem;
		background-color: var(--gold);
		flex-shrink: 0;
		align-self: center;
	}

	.verse-line__ajz {
		flex: 1;
		text-align: right;
	}

	.poem-card__link {
		display: inline-flex;
		align-items: center;
		min-height: 44px;
		font-family: var(--font-ui);
		font-size: 0.95rem;
		color: var(--gold);
		text-decoration: none;
		border-bottom: 1px solid transparent;
		transition: border-color 0.2s ease;
	}

	.poem-card__link:hover {
		border-bottom-color: var(--gold);
	}

	/* ========================================
	   STATS BAR
	   ======================================== */
	.stats {
		background-color: var(--leather);
		padding: 3rem 2rem;
	}

	.stats__inner {
		max-width: 900px;
		margin: 0 auto;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 3rem;
		flex-wrap: wrap;
	}

	.stats__item {
		text-align: center;
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
	}

	.stats__number {
		font-family: var(--font-heading);
		font-size: clamp(1.8rem, 4vw, 2.5rem);
		font-weight: 700;
		color: var(--gold);
	}

	.stats__label {
		font-family: var(--font-ui);
		font-size: 1rem;
		color: var(--gold-light);
		opacity: 0.85;
	}

	.stats__separator {
		width: 1px;
		height: 3rem;
		background: linear-gradient(180deg, transparent, var(--gold), transparent);
	}

	/* ========================================
	   ABOUT SECTION
	   ======================================== */
	.about {
		padding: 6rem 2rem;
		background-color: var(--papyrus);
		background-image:
			repeating-linear-gradient(
				45deg,
				transparent,
				transparent 3px,
				rgba(44, 24, 16, 0.008) 3px,
				rgba(44, 24, 16, 0.008) 6px
			);
	}

	.about__inner {
		max-width: 1100px;
		margin: 0 auto;
		display: flex;
		align-items: center;
		gap: 4rem;
	}

	.about__medallion {
		flex-shrink: 0;
		width: 280px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.shamsa {
		width: 100%;
		height: auto;
		opacity: 0.7;
	}

	.about__text {
		flex: 1;
	}

	.about__title {
		font-family: var(--font-heading);
		font-size: clamp(1.8rem, 4vw, 2.5rem);
		font-weight: 700;
		color: var(--ink);
		margin: 0 0 1.5rem;
	}

	.about__bio {
		font-family: var(--font-body);
		font-size: 1.15rem;
		line-height: 2.2;
		color: var(--ink);
		margin: 0;
	}

	.about__bio::first-letter {
		font-family: var(--font-heading);
		font-size: 3.5rem;
		font-weight: 700;
		float: right;
		line-height: 1;
		margin-left: 0.75rem;
		margin-bottom: 0.25rem;
		color: var(--burgundy);
	}

	/* ========================================
	   FOOTER
	   ======================================== */
	.footer {
		background-color: var(--leather);
		padding: 3rem 2rem;
		text-align: center;
	}

	.footer__inner {
		max-width: 800px;
		margin: 0 auto;
	}

	.footer__motif {
		width: 80px;
		height: auto;
		margin: 0 auto 1.5rem;
		display: block;
	}

	.footer__name {
		font-family: var(--font-heading);
		font-size: 1.5rem;
		font-weight: 700;
		color: var(--gold);
		margin: 0 0 0.5rem;
	}

	.footer__copy {
		font-family: var(--font-ui);
		font-size: 0.9rem;
		color: var(--gold-light);
		opacity: 0.7;
		margin: 0 0 1.5rem;
	}

	.footer__links {
		list-style: none;
		margin: 0;
		padding: 0;
		display: flex;
		justify-content: center;
		gap: 2rem;
		flex-wrap: wrap;
	}

	.footer__links a {
		font-family: var(--font-ui);
		font-size: 0.95rem;
		color: var(--gold-light);
		text-decoration: none;
		min-height: 44px;
		display: flex;
		align-items: center;
		transition: color 0.2s ease;
	}

	.footer__links a:hover {
		color: var(--gold);
	}

	/* ========================================
	   RESPONSIVE
	   ======================================== */
	@media (max-width: 1024px) {
		.poems__grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.about__medallion {
			width: 220px;
		}
	}

	@media (max-width: 768px) {
		.poems__grid {
			grid-template-columns: 1fr;
			max-width: 500px;
		}

		.about__inner {
			flex-direction: column;
			text-align: center;
		}

		.about__medallion {
			width: 200px;
		}

		.about__bio::first-letter {
			float: none;
			margin-left: 0;
		}

		.nav__links {
			gap: 1rem;
		}

		.stats__inner {
			gap: 2rem;
		}

		.stats__separator {
			display: none;
		}
	}

	@media (max-width: 480px) {
		.nav__inner {
			flex-direction: column;
			gap: 0.75rem;
		}

		.hero__verse {
			flex-direction: column;
			gap: 0.5rem;
		}

		.hero__verse-divider {
			width: 3rem;
			height: 1px;
		}

		.hero__verse-sadr,
		.hero__verse-ajz {
			text-align: center;
		}

		.verse-line {
			flex-direction: column;
			gap: 0;
			text-align: center;
		}

		.verse-line__sadr,
		.verse-line__ajz {
			text-align: center;
		}

		.verse-line__divider {
			display: none;
		}

		.nav__links {
			gap: 0.75rem;
		}

		.footer__links {
			gap: 1rem;
		}
	}

	/* ========================================
	   REDUCED MOTION
	   ======================================== */
	@media (prefers-reduced-motion: reduce) {
		.nav {
			transition: none;
		}

		.hero__cta {
			transition: none;
		}

		.poem-card {
			transition: none;
		}

		.poem-card:hover {
			transform: none;
		}

		.nav__link::after {
			transition: none;
		}

		.poem-card__link {
			transition: none;
		}

		.footer__links a {
			transition: none;
		}
	}
</style>
