<script lang="ts">
	import { featuredPoems, bioTextShort, categories } from '$lib/utils/poems';
</script>

<svelte:head>
	<title>سمير الشيخ - تراث الصحراء</title>
</svelte:head>

<!-- Navigation -->
<nav class="nav-bar">
	<div class="nav-inner">
		<a href="#hero" class="nav-logo">سمير الشيخ</a>
		<ul class="nav-links">
			<li><a href="#hero" class="active">الرئيسية</a></li>
			<li><a href="#poems">الديوان</a></li>
			<li><a href="#about">عن الشاعر</a></li>
			<li><a href="#footer">تواصل</a></li>
		</ul>
	</div>
</nav>

<!-- Hero Section -->
<section id="hero" class="hero">
	<!-- Top Sadu Band -->
	<svg class="sadu-band" viewBox="0 0 1200 50" preserveAspectRatio="none" aria-hidden="true">
		<rect width="1200" height="50" fill="#E8D5B8" />
		<!-- Row of diamonds -->
		{#each Array(24) as _, i}
			<polygon
				points="{i * 50 + 25},5 {i * 50 + 45},25 {i * 50 + 25},45 {i * 50 + 5},25"
				fill="none"
				stroke="#C4883A"
				stroke-width="2"
			/>
			<polygon
				points="{i * 50 + 25},12 {i * 50 + 38},25 {i * 50 + 25},38 {i * 50 + 12},25"
				fill="#8B3A2A"
				opacity="0.7"
			/>
		{/each}
		<!-- Zigzag lines -->
		<polyline
			points={Array(49)
				.fill(0)
				.map((_, i) => `${i * 25},${i % 2 === 0 ? 3 : 15}`)
				.join(' ')}
			fill="none"
			stroke="#2C1810"
			stroke-width="1.5"
		/>
		<polyline
			points={Array(49)
				.fill(0)
				.map((_, i) => `${i * 25},${i % 2 === 0 ? 35 : 47}`)
				.join(' ')}
			fill="none"
			stroke="#2C1810"
			stroke-width="1.5"
		/>
	</svg>

	<div class="hero-content">
		<h1 class="hero-name">سمير الشيخ</h1>
		<p class="hero-subtitle">شاعر من صحراء الكلمات</p>

		<div class="hero-verse">
			<div class="verse-line">
				<span class="sadr">بلادي وإن جارَت عليَّ عزيزةٌ</span>
				<span class="verse-divider"></span>
				<span class="ajz">وأهلي وإن ضنّوا عليَّ كِرامُ</span>
			</div>
		</div>

		<a href="#poems" class="hero-cta">استكشف الديوان</a>
	</div>

	<!-- Bottom Sadu Band -->
	<svg class="sadu-band sadu-bottom" viewBox="0 0 1200 50" preserveAspectRatio="none" aria-hidden="true">
		<rect width="1200" height="50" fill="#C49A6C" />
		{#each Array(24) as _, i}
			<polygon
				points="{i * 50 + 25},5 {i * 50 + 45},25 {i * 50 + 25},45 {i * 50 + 5},25"
				fill="none"
				stroke="#2C1810"
				stroke-width="2"
			/>
			<polygon
				points="{i * 50 + 25},15 {i * 50 + 35},25 {i * 50 + 25},35 {i * 50 + 15},25"
				fill="#C4883A"
			/>
		{/each}
		<polyline
			points={Array(49)
				.fill(0)
				.map((_, i) => `${i * 25},${i % 2 === 0 ? 3 : 15}`)
				.join(' ')}
			fill="none"
			stroke="#8B3A2A"
			stroke-width="1.5"
		/>
		<polyline
			points={Array(49)
				.fill(0)
				.map((_, i) => `${i * 25},${i % 2 === 0 ? 35 : 47}`)
				.join(' ')}
			fill="none"
			stroke="#8B3A2A"
			stroke-width="1.5"
		/>
	</svg>
</section>

<!-- Featured Poems Section -->
<section id="poems" class="poems-section">
	<!-- Sadu Divider -->
	<svg class="sadu-divider" viewBox="0 0 1200 40" preserveAspectRatio="none" aria-hidden="true">
		<rect width="1200" height="40" fill="#F5EDE0" />
		{#each Array(30) as _, i}
			<polygon
				points="{i * 40 + 20},4 {i * 40 + 36},20 {i * 40 + 20},36 {i * 40 + 4},20"
				fill="none"
				stroke="#C4883A"
				stroke-width="1.5"
			/>
			<polygon
				points="{i * 40 + 20},10 {i * 40 + 30},20 {i * 40 + 20},30 {i * 40 + 10},20"
				fill="#8B3A2A"
				opacity="0.5"
			/>
		{/each}
		<line x1="0" y1="1" x2="1200" y2="1" stroke="#C4883A" stroke-width="2" />
		<line x1="0" y1="39" x2="1200" y2="39" stroke="#C4883A" stroke-width="2" />
	</svg>

	<div class="section-container">
		<h2 class="section-title">من روائع القصائد</h2>

		<div class="poems-grid">
			{#each featuredPoems as poem}
				<article class="poem-card">
					<h3 class="poem-title">{poem.title}</h3>
					<span class="poem-category">{categories[poem.category]}</span>

					<div class="poem-verses">
						{#each poem.verses.slice(0, 2) as verse}
							<div class="verse-line">
								<span class="sadr">{verse.sadr}</span>
								<span class="verse-divider"></span>
								<span class="ajz">{verse.ajz}</span>
							</div>
						{/each}
					</div>

					<a href="/sample/desert" class="poem-link">اقرأ القصيدة</a>
				</article>
			{/each}
		</div>
	</div>
</section>

<!-- Stats Section -->
<section class="stats-section">
	<div class="stats-container">
		<div class="stat-item">
			<span class="stat-number">٣٠٠+</span>
			<span class="stat-label">قصيدة</span>
		</div>
		<div class="stat-item">
			<span class="stat-number">٥٠+</span>
			<span class="stat-label">سنة من الشعر</span>
		</div>
		<div class="stat-item">
			<span class="stat-number">٩</span>
			<span class="stat-label">أبواب شعرية</span>
		</div>
	</div>
</section>

<!-- About Preview -->
<section id="about" class="about-section">
	<div class="about-container">
		<div class="about-text">
			<h2 class="section-title">عن الشاعر</h2>
			<p class="about-bio">{bioTextShort}</p>
			<a href="/sample/desert" class="about-link">اقرأ المزيد</a>
		</div>

		<div class="about-decoration">
			<svg viewBox="0 0 300 300" class="desert-scene" aria-hidden="true">
				<!-- Outer Sadu-inspired circular frame -->
				<circle cx="150" cy="150" r="145" fill="none" stroke="#C4883A" stroke-width="3" />
				<circle cx="150" cy="150" r="138" fill="none" stroke="#8B3A2A" stroke-width="1.5" stroke-dasharray="8 4" />
				<circle cx="150" cy="150" r="132" fill="none" stroke="#C4883A" stroke-width="1" />

				<!-- Night sky background -->
				<clipPath id="circleClip">
					<circle cx="150" cy="150" r="130" />
				</clipPath>
				<g clip-path="url(#circleClip)">
					<rect x="0" y="0" width="300" height="300" fill="#1A2744" />

					<!-- Stars -->
					<circle cx="60" cy="50" r="1.5" fill="#FFFDE8" />
					<circle cx="100" cy="80" r="1" fill="#FFFDE8" />
					<circle cx="200" cy="40" r="1.5" fill="#FFFDE8" />
					<circle cx="240" cy="70" r="1" fill="#FFFDE8" />
					<circle cx="170" cy="60" r="1.2" fill="#FFFDE8" />
					<circle cx="80" cy="100" r="0.8" fill="#FFFDE8" />
					<circle cx="130" cy="45" r="1" fill="#FFFDE8" />
					<circle cx="220" cy="95" r="0.8" fill="#FFFDE8" />
					<circle cx="50" cy="120" r="1" fill="#FFFDE8" />
					<circle cx="260" cy="55" r="1.2" fill="#FFFDE8" />
					<circle cx="185" cy="90" r="0.7" fill="#FFFDE8" />
					<circle cx="110" cy="115" r="0.9" fill="#FFFDE8" />
					<circle cx="145" cy="70" r="1.3" fill="#FFFDE8" />
					<circle cx="75" cy="65" r="0.6" fill="#FFFDE8" />
					<circle cx="230" cy="110" r="1.1" fill="#FFFDE8" />

					<!-- Crescent Moon -->
					<circle cx="220" cy="80" r="28" fill="#C4883A" />
					<circle cx="232" cy="72" r="24" fill="#1A2744" />

					<!-- Desert dunes -->
					<path d="M0,200 Q75,160 150,190 Q225,220 300,180 L300,300 L0,300 Z" fill="#C49A6C" opacity="0.6" />
					<path d="M0,220 Q100,185 200,210 Q260,230 300,200 L300,300 L0,300 Z" fill="#D4A96A" opacity="0.7" />
					<path d="M0,240 Q80,215 160,235 Q240,255 300,225 L300,300 L0,300 Z" fill="#E8D5B8" opacity="0.8" />
				</g>

				<!-- Diamond accents on frame -->
				{#each [0, 45, 90, 135, 180, 225, 270, 315] as angle}
					<polygon
						points="0,-8 5,0 0,8 -5,0"
						fill="#C4883A"
						transform="translate({150 + 142 * Math.cos((angle * Math.PI) / 180)}, {150 + 142 * Math.sin((angle * Math.PI) / 180)}) rotate({angle})"
					/>
				{/each}
			</svg>
		</div>
	</div>
</section>

<!-- Footer -->
<footer id="footer" class="site-footer">
	<!-- Sadu strip at top of footer -->
	<svg class="sadu-divider footer-sadu" viewBox="0 0 1200 40" preserveAspectRatio="none" aria-hidden="true">
		<rect width="1200" height="40" fill="#1A2744" />
		{#each Array(30) as _, i}
			<polygon
				points="{i * 40 + 20},4 {i * 40 + 36},20 {i * 40 + 20},36 {i * 40 + 4},20"
				fill="none"
				stroke="#C4883A"
				stroke-width="1.5"
			/>
		{/each}
		<line x1="0" y1="1" x2="1200" y2="1" stroke="#C4883A" stroke-width="1" />
		<line x1="0" y1="39" x2="1200" y2="39" stroke="#C4883A" stroke-width="1" />
	</svg>

	<div class="footer-content">
		<p class="footer-name">سمير الشيخ</p>
		<p class="footer-copy">جميع الحقوق محفوظة</p>
		<ul class="footer-links">
			<li><a href="#hero">الرئيسية</a></li>
			<li><a href="#poems">الديوان</a></li>
			<li><a href="#about">عن الشاعر</a></li>
			<li><a href="#footer">تواصل</a></li>
		</ul>
	</div>
</footer>

<style>
	/* ===== Base & Variables ===== */
	:global(body) {
		margin: 0;
		padding: 0;
	}

	*,
	*::before,
	*::after {
		box-sizing: border-box;
	}

	:root {
		--dune-cream: #f5ede0;
		--deep-umber: #2c1810;
		--sunset-gold: #c4883a;
		--henna-red: #8b3a2a;
		--desert-night: #1a2744;
		--warm-dark: #3d2b1f;
		--card-bg: #fffdf8;
		--font-heading: 'Amiri', serif;
		--font-body: 'Noto Naskh Arabic', serif;
	}

	/* ===== Sand Texture Background ===== */
	section,
	.about-section {
		position: relative;
	}

	/* ===== Navigation ===== */
	.nav-bar {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 100;
		background: rgba(245, 237, 224, 0.9);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		border-bottom: 1px solid rgba(196, 136, 58, 0.2);
	}

	.nav-inner {
		max-width: 1200px;
		margin: 0 auto;
		padding: 0.75rem 2rem;
		display: flex;
		align-items: center;
		justify-content: space-between;
		direction: rtl;
	}

	.nav-logo {
		font-family: var(--font-heading);
		font-weight: 700;
		font-size: 1.5rem;
		color: var(--deep-umber);
		text-decoration: none;
	}

	.nav-links {
		list-style: none;
		margin: 0;
		padding: 0;
		display: flex;
		gap: 2rem;
	}

	.nav-links a {
		font-family: var(--font-heading);
		font-size: 1.05rem;
		color: var(--deep-umber);
		text-decoration: none;
		padding: 0.5rem 0;
		position: relative;
		transition: color 0.3s ease;
		min-height: 44px;
		display: flex;
		align-items: center;
	}

	.nav-links a::after {
		content: '';
		position: absolute;
		bottom: 0;
		right: 0;
		width: 0;
		height: 2px;
		background: var(--sunset-gold);
		transition: width 0.3s ease;
	}

	.nav-links a:hover,
	.nav-links a.active {
		color: var(--sunset-gold);
	}

	.nav-links a:hover::after,
	.nav-links a.active::after {
		width: 100%;
	}

	/* ===== Hero Section ===== */
	.hero {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		background: linear-gradient(180deg, #e8d5b8 0%, #d4a96a 50%, #c49a6c 100%);
		position: relative;
		overflow: hidden;
		direction: rtl;
		padding-top: 60px;
	}

	.hero::before {
		content: '';
		position: absolute;
		inset: 0;
		background:
			repeating-linear-gradient(
				45deg,
				transparent,
				transparent 2px,
				rgba(44, 24, 16, 0.02) 2px,
				rgba(44, 24, 16, 0.02) 4px
			);
		pointer-events: none;
	}

	.sadu-band {
		width: 100%;
		height: 50px;
		display: block;
		position: absolute;
		top: 60px;
		left: 0;
	}

	.sadu-bottom {
		top: auto;
		bottom: 0;
	}

	.hero-content {
		text-align: center;
		z-index: 1;
		padding: 2rem;
	}

	.hero-name {
		font-family: var(--font-heading);
		font-weight: 700;
		font-size: 4.5rem;
		color: var(--deep-umber);
		margin: 0 0 0.5rem;
		line-height: 1.2;
	}

	.hero-subtitle {
		font-family: var(--font-body);
		font-size: 1.5rem;
		color: var(--warm-dark);
		margin: 0 0 2.5rem;
		opacity: 0.85;
	}

	.hero-verse {
		margin-bottom: 2.5rem;
	}

	.hero-verse .verse-line {
		font-size: 1.3rem;
	}

	.hero-cta {
		display: inline-block;
		font-family: var(--font-heading);
		font-size: 1.15rem;
		font-weight: 700;
		color: var(--deep-umber);
		border: 2px solid var(--sunset-gold);
		padding: 0.85rem 2.5rem;
		text-decoration: none;
		border-radius: 4px;
		transition: background-color 0.3s ease, color 0.3s ease;
		min-height: 44px;
		min-width: 44px;
	}

	.hero-cta:hover {
		background: var(--sunset-gold);
		color: #fff;
	}

	/* ===== Verse Layout (Two-Hemistich) ===== */
	.verse-line {
		display: grid;
		grid-template-columns: 1fr 2px 1fr;
		gap: 1rem;
		align-items: center;
		font-family: var(--font-body);
		font-size: 1.1rem;
		line-height: 2.2;
		direction: rtl;
		margin-bottom: 0.25rem;
	}

	.sadr {
		text-align: center;
	}

	.ajz {
		text-align: center;
	}

	.verse-divider {
		width: 2px;
		height: 1.5em;
		background: var(--sunset-gold);
		margin: 0 auto;
		border-radius: 1px;
	}

	/* ===== Sadu Divider ===== */
	.sadu-divider {
		width: 100%;
		height: 40px;
		display: block;
	}

	/* ===== Poems Section ===== */
	.poems-section {
		background-color: var(--dune-cream);
		background-image:
			repeating-linear-gradient(
				0deg,
				transparent,
				transparent 3px,
				rgba(44, 24, 16, 0.01) 3px,
				rgba(44, 24, 16, 0.01) 6px
			),
			repeating-linear-gradient(
				90deg,
				transparent,
				transparent 3px,
				rgba(44, 24, 16, 0.01) 3px,
				rgba(44, 24, 16, 0.01) 6px
			);
		padding: 0 0 5rem;
		direction: rtl;
	}

	.section-container {
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 2rem;
	}

	.section-title {
		font-family: var(--font-heading);
		font-weight: 700;
		font-size: 2.2rem;
		color: var(--deep-umber);
		text-align: center;
		margin: 3rem 0 2.5rem;
	}

	.poems-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
	}

	.poem-card {
		background: var(--card-bg);
		border-radius: 8px;
		padding: 2rem;
		box-shadow: 0 2px 12px rgba(44, 24, 16, 0.08);
		border-right: 4px solid transparent;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.poem-card:hover {
		border-right-color: var(--sunset-gold);
		box-shadow: 0 4px 20px rgba(44, 24, 16, 0.14);
	}

	.poem-title {
		font-family: var(--font-heading);
		font-weight: 700;
		font-size: 1.4rem;
		color: var(--deep-umber);
		margin: 0 0 0.75rem;
	}

	.poem-category {
		display: inline-block;
		font-family: var(--font-body);
		font-size: 0.85rem;
		background: rgba(196, 136, 58, 0.15);
		color: var(--warm-dark);
		padding: 0.25rem 0.85rem;
		border-radius: 20px;
		margin-bottom: 1.25rem;
	}

	.poem-verses {
		margin-bottom: 1.25rem;
	}

	.poem-verses .verse-line {
		font-size: 0.95rem;
	}

	.poem-link {
		font-family: var(--font-heading);
		font-size: 1rem;
		color: var(--henna-red);
		text-decoration: none;
		font-weight: 700;
		transition: color 0.3s ease;
		min-height: 44px;
		display: inline-flex;
		align-items: center;
	}

	.poem-link:hover {
		color: var(--sunset-gold);
	}

	/* ===== Stats Section ===== */
	.stats-section {
		background: var(--warm-dark);
		padding: 4rem 2rem;
		direction: rtl;
	}

	.stats-container {
		max-width: 1000px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
		text-align: center;
	}

	.stat-item {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.stat-number {
		font-family: var(--font-heading);
		font-weight: 700;
		font-size: 3rem;
		color: var(--sunset-gold);
		line-height: 1.1;
	}

	.stat-label {
		font-family: var(--font-body);
		font-size: 1.1rem;
		color: rgba(255, 255, 255, 0.85);
	}

	/* ===== About Section ===== */
	.about-section {
		background-color: var(--dune-cream);
		background-image:
			repeating-linear-gradient(
				0deg,
				transparent,
				transparent 3px,
				rgba(44, 24, 16, 0.01) 3px,
				rgba(44, 24, 16, 0.01) 6px
			),
			repeating-linear-gradient(
				90deg,
				transparent,
				transparent 3px,
				rgba(44, 24, 16, 0.01) 3px,
				rgba(44, 24, 16, 0.01) 6px
			);
		padding: 5rem 2rem;
		direction: rtl;
	}

	.about-container {
		max-width: 1100px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 4rem;
		align-items: center;
	}

	.about-bio {
		font-family: var(--font-body);
		font-size: 1.15rem;
		line-height: 2;
		color: var(--deep-umber);
		margin: 0 0 2rem;
	}

	.about-link {
		font-family: var(--font-heading);
		font-size: 1.05rem;
		font-weight: 700;
		color: var(--henna-red);
		text-decoration: none;
		border-bottom: 2px solid transparent;
		transition: border-color 0.3s ease;
		min-height: 44px;
		display: inline-flex;
		align-items: center;
	}

	.about-link:hover {
		border-bottom-color: var(--henna-red);
	}

	.about-decoration {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.desert-scene {
		width: 100%;
		max-width: 300px;
		height: auto;
	}

	/* ===== Footer ===== */
	.site-footer {
		background: var(--desert-night);
		position: relative;
		overflow: hidden;
		direction: rtl;
	}

	.site-footer::before {
		content: '';
		position: absolute;
		inset: 0;
		background:
			radial-gradient(1px 1px at 10% 15%, rgba(255, 255, 255, 0.6), transparent),
			radial-gradient(1px 1px at 25% 35%, rgba(255, 255, 255, 0.5), transparent),
			radial-gradient(1.5px 1.5px at 40% 10%, rgba(255, 255, 255, 0.7), transparent),
			radial-gradient(1px 1px at 55% 45%, rgba(255, 255, 255, 0.4), transparent),
			radial-gradient(1px 1px at 70% 20%, rgba(255, 255, 255, 0.6), transparent),
			radial-gradient(1.5px 1.5px at 85% 40%, rgba(255, 255, 255, 0.5), transparent),
			radial-gradient(1px 1px at 15% 55%, rgba(255, 255, 255, 0.4), transparent),
			radial-gradient(1px 1px at 35% 65%, rgba(255, 255, 255, 0.5), transparent),
			radial-gradient(1.5px 1.5px at 50% 75%, rgba(255, 255, 255, 0.6), transparent),
			radial-gradient(1px 1px at 65% 55%, rgba(255, 255, 255, 0.4), transparent),
			radial-gradient(1px 1px at 80% 70%, rgba(255, 255, 255, 0.5), transparent),
			radial-gradient(1px 1px at 90% 60%, rgba(255, 255, 255, 0.3), transparent),
			radial-gradient(1px 1px at 5% 80%, rgba(255, 255, 255, 0.4), transparent),
			radial-gradient(1.5px 1.5px at 20% 90%, rgba(255, 255, 255, 0.5), transparent),
			radial-gradient(1px 1px at 45% 85%, rgba(255, 255, 255, 0.3), transparent),
			radial-gradient(1px 1px at 60% 92%, rgba(255, 255, 255, 0.4), transparent),
			radial-gradient(1px 1px at 75% 88%, rgba(255, 255, 255, 0.5), transparent),
			radial-gradient(1.5px 1.5px at 95% 82%, rgba(255, 255, 255, 0.6), transparent);
		pointer-events: none;
	}

	.footer-sadu {
		position: relative;
	}

	.footer-content {
		max-width: 1000px;
		margin: 0 auto;
		padding: 4rem 2rem;
		text-align: center;
		position: relative;
		z-index: 1;
	}

	.footer-name {
		font-family: var(--font-heading);
		font-weight: 700;
		font-size: 1.8rem;
		color: var(--sunset-gold);
		margin: 0 0 0.5rem;
	}

	.footer-copy {
		font-family: var(--font-body);
		font-size: 0.95rem;
		color: rgba(255, 255, 255, 0.6);
		margin: 0 0 2rem;
	}

	.footer-links {
		list-style: none;
		margin: 0;
		padding: 0;
		display: flex;
		justify-content: center;
		gap: 2rem;
	}

	.footer-links a {
		font-family: var(--font-heading);
		font-size: 1rem;
		color: var(--sunset-gold);
		text-decoration: none;
		transition: opacity 0.3s ease;
		min-height: 44px;
		display: inline-flex;
		align-items: center;
	}

	.footer-links a:hover {
		opacity: 0.75;
	}

	/* ===== Reduced Motion ===== */
	@media (prefers-reduced-motion: reduce) {
		*,
		*::before,
		*::after {
			transition-duration: 0.01ms !important;
			animation-duration: 0.01ms !important;
		}
	}

	/* ===== Responsive: Tablet (768px) ===== */
	@media (max-width: 1024px) {
		.poems-grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.about-container {
			gap: 2.5rem;
		}
	}

	@media (max-width: 768px) {
		.hero-name {
			font-size: 3rem;
		}

		.hero-subtitle {
			font-size: 1.2rem;
		}

		.poems-grid {
			grid-template-columns: 1fr;
		}

		.about-container {
			grid-template-columns: 1fr;
		}

		.about-decoration {
			order: -1;
		}

		.desert-scene {
			max-width: 220px;
		}

		.stats-container {
			grid-template-columns: 1fr;
			gap: 2.5rem;
		}

		.stat-number {
			font-size: 2.4rem;
		}

		.nav-links {
			gap: 1rem;
		}

		.nav-links a {
			font-size: 0.9rem;
		}

		.section-title {
			font-size: 1.8rem;
		}

		.verse-line {
			grid-template-columns: 1fr;
			gap: 0;
			text-align: center;
		}

		.verse-divider {
			display: none;
		}

		.footer-links {
			flex-wrap: wrap;
			gap: 1rem;
		}
	}

	@media (max-width: 480px) {
		.hero-name {
			font-size: 2.4rem;
		}

		.hero-subtitle {
			font-size: 1rem;
		}

		.nav-inner {
			padding: 0.75rem 1rem;
			flex-direction: column;
			gap: 0.5rem;
		}

		.nav-links {
			gap: 0.75rem;
		}

		.poem-card {
			padding: 1.5rem;
		}

		.footer-content {
			padding: 3rem 1.5rem;
		}
	}
</style>
