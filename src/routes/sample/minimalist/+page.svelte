<script lang="ts">
	import { onMount } from 'svelte';
	import { featuredPoems, bioText, categories } from '$lib/utils/poems';

	let heroVisible = $state(false);

	onMount(() => {
		const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
		if (mediaQuery.matches) {
			heroVisible = true;
		} else {
			requestAnimationFrame(() => {
				heroVisible = true;
			});
		}
	});

	const navLinks = [
		{ label: 'الديوان', href: '#poems' },
		{ label: 'عن الشاعر', href: '#about' },
		{ label: 'تواصل', href: '#contact' }
	];

	let activeLink = $state('#hero');

	function handleNavClick(href: string) {
		activeLink = href;
	}

	const heroVerse = featuredPoems[0]?.verses[0];
</script>


<div class="page" dir="rtl" lang="ar">
	<!-- Navigation -->
	<nav class="nav">
		<div class="nav-inner">
			<a href="/sample/minimalist" class="nav-logo">سمير الشيخ حسين</a>
			<div class="nav-links">
				{#each navLinks as link}
					<a
						href={link.href}
						class="nav-link"
						class:active={activeLink === link.href}
						onclick={() => handleNavClick(link.href)}
					>
						{link.label}
					</a>
				{/each}
			</div>
		</div>
	</nav>

	<!-- Hero Section -->
	<section id="hero" class="hero" class:hero-visible={heroVisible}>
		<div class="hero-content">
			<div class="rule"></div>
			<h1 class="hero-name">سمير الشيخ</h1>
			<p class="hero-subtitle">شاعر عربي</p>

			{#if heroVerse}
				<div class="hero-verse">
					<div class="verse-line">
						<span class="sadr">{heroVerse.sadr}</span>
						<span class="verse-divider"></span>
						<span class="ajz">{heroVerse.ajz}</span>
					</div>
				</div>
			{/if}

			<div class="rule"></div>
			<a href="#poems" class="explore-link" onclick={() => handleNavClick('#poems')}>
				استكشف الديوان
				<span class="arrow" aria-hidden="true">&larr;</span>
			</a>
		</div>
	</section>

	<!-- Featured Poems Section -->
	<section id="poems" class="poems-section">
		<div class="section-container">
			<div class="rule"></div>
			<h2 class="section-title">من الديوان</h2>

			<div class="poems-grid">
				{#each featuredPoems as poem}
					<article class="poem-card">
						<h3 class="poem-title">{poem.title}</h3>
						<span class="poem-category">{categories[poem.category] ?? poem.category}</span>

						<div class="poem-verses">
							{#each poem.verses.slice(0, 2) as verse}
								<div class="verse-line">
									<span class="sadr">{verse.sadr}</span>
									<span class="verse-divider"></span>
									<span class="ajz">{verse.ajz}</span>
								</div>
							{/each}
						</div>

						<a href="#poems" class="read-more">اقرأ المزيد</a>
					</article>
				{/each}
			</div>
		</div>
	</section>

	<!-- Stats Section -->
	<section class="stats-section">
		<div class="stats-container">
			<div class="stat">
				<span class="stat-number">٣٠٠+</span>
				<span class="stat-label">قصيدة</span>
			</div>
			<div class="stat">
				<span class="stat-number">٥٠+</span>
				<span class="stat-label">سنة من الشعر</span>
			</div>
			<div class="stat">
				<span class="stat-number">٩</span>
				<span class="stat-label">أبواب شعرية</span>
			</div>
		</div>
	</section>

	<!-- About Preview -->
	<section id="about" class="about-section">
		<div class="about-container">
			<h2 class="section-title">عن الشاعر</h2>
			<div class="rule"></div>
			<p class="about-text">{bioText}</p>
			<a href="#about" class="read-more">المزيد</a>
		</div>
	</section>

	<!-- Footer -->
	<footer id="contact" class="footer">
		<div class="footer-inner">
			<p class="footer-name">سمير الشيخ حسين</p>
			<p class="footer-copy">جميع الحقوق محفوظة ٢٠٢٦</p>
			<nav class="footer-nav">
				{#each navLinks as link}
					<a href={link.href} class="footer-link">{link.label}</a>
				{/each}
			</nav>
		</div>
	</footer>
</div>

<style>
	/* ============================================
	   Modern Minimalist - الأناقة المعاصرة
	   ============================================ */

	:global(body) {
		margin: 0;
		padding: 0;
	}

	.page {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 18px;
		line-height: 1.8;
		color: #2c2925;
		background-color: #fafaf7;
		direction: rtl;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
	}

	/* ---------- Navigation ---------- */

	.nav {
		position: sticky;
		top: 0;
		z-index: 100;
		background-color: rgba(250, 250, 247, 0.95);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		border-bottom: 1px solid #e0ddd8;
	}

	.nav-inner {
		max-width: 1200px;
		margin: 0 auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1.25rem 2rem;
	}

	.nav-logo {
		font-family: 'Amiri', serif;
		font-size: 1.6rem;
		font-weight: 700;
		color: #2c2925;
		text-decoration: none;
		white-space: nowrap;
		min-height: 44px;
		display: flex;
		align-items: center;
		letter-spacing: 0.01em;
	}

	.nav-links {
		display: flex;
		gap: 3rem;
	}

	.nav-link {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.9rem;
		font-weight: 500;
		color: #2c2925;
		text-decoration: none;
		padding: 0.5rem 0;
		position: relative;
		transition: color 0.2s ease;
		min-height: 44px;
		display: flex;
		align-items: center;
	}

	.nav-link::after {
		content: '';
		position: absolute;
		bottom: 0;
		right: 0;
		left: 0;
		height: 2px;
		background-color: #7a2532;
		transform: scaleX(0);
		transition: transform 0.2s ease;
	}

	.nav-link:hover {
		color: #7a2532;
	}

	.nav-link.active::after {
		transform: scaleX(1);
	}

	.nav-link.active {
		color: #7a2532;
	}

	/* ---------- Burgundy Rule ---------- */

	.rule {
		width: 80px;
		height: 2px;
		background-color: #7a2532;
		margin: 0 auto;
	}

	/* ---------- Hero Section ---------- */

	.hero {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #fafaf7;
		padding: 6rem 2rem;
		box-sizing: border-box;
	}

	.hero-content {
		text-align: center;
		opacity: 0;
		transform: translateY(20px);
		transition: opacity 1s ease, transform 1s ease;
	}

	.hero-visible .hero-content {
		opacity: 1;
		transform: translateY(0);
	}

	@media (prefers-reduced-motion: reduce) {
		.hero-content {
			opacity: 1;
			transform: none;
			transition: none;
		}
	}

	.hero-name {
		font-family: 'Amiri', serif;
		font-size: 4.5rem;
		font-weight: 700;
		color: #2c2925;
		margin: 2rem 0 0.5rem;
		line-height: 1.2;
	}

	.hero-subtitle {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 1.2rem;
		font-weight: 300;
		color: #6b6560;
		margin: 0 0 3rem;
		letter-spacing: 0.02em;
	}

	.hero-verse {
		margin: 3rem auto;
		max-width: 700px;
	}

	.explore-link {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.95rem;
		font-weight: 500;
		color: #7a2532;
		text-decoration: none;
		margin-top: 2rem;
		padding: 0.5rem 0;
		min-height: 44px;
		transition: gap 0.2s ease;
	}

	.explore-link:hover {
		gap: 0.75rem;
	}

	.arrow {
		font-size: 1.2rem;
		line-height: 1;
	}

	/* ---------- Verse Layout (Two-Hemistich) ---------- */

	.verse-line {
		display: grid;
		grid-template-columns: 1fr auto 1fr;
		align-items: center;
		gap: 1.5rem;
		padding: 0.8rem 0;
	}

	.sadr {
		font-family: 'Amiri', serif;
		font-size: 1.15rem;
		line-height: 2.4;
		text-align: center;
	}

	.ajz {
		font-family: 'Amiri', serif;
		font-size: 1.15rem;
		line-height: 2.4;
		text-align: center;
	}

	.verse-divider {
		width: 1px;
		height: 2rem;
		background-color: #7a2532;
		opacity: 0.5;
	}

	/* ---------- Featured Poems Section ---------- */

	.poems-section {
		padding: 6rem 2rem;
		background-color: #f2f0eb;
	}

	.section-container {
		max-width: 900px;
		margin: 0 auto;
	}

	.section-title {
		font-family: 'Amiri', serif;
		font-size: 2.2rem;
		font-weight: 700;
		color: #2c2925;
		text-align: center;
		margin: 1.5rem 0 3rem;
	}

	.poems-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 2rem;
		margin-top: 2rem;
	}

	.poem-card {
		border: 1px solid #e0ddd8;
		border-radius: 4px;
		padding: 2.5rem 2rem;
		background-color: #fafaf7;
		transition: border-color 0.2s ease;
	}

	.poem-card:hover {
		border-color: #7a2532;
	}

	.poem-title {
		font-family: 'Amiri', serif;
		font-size: 1.5rem;
		font-weight: 700;
		color: #2c2925;
		margin: 0 0 0.5rem;
	}

	.poem-category {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.8rem;
		font-weight: 500;
		color: #6b6560;
		display: inline-block;
		margin-bottom: 1.5rem;
	}

	.poem-verses {
		margin-bottom: 1.5rem;
	}

	.poem-verses .verse-line {
		gap: 1rem;
	}

	.poem-verses .sadr,
	.poem-verses .ajz {
		font-size: 1rem;
	}

	.read-more {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.9rem;
		font-weight: 500;
		color: #7a2532;
		text-decoration: none;
		transition: opacity 0.2s ease;
		display: inline-block;
		min-height: 44px;
		line-height: 44px;
	}

	.read-more:hover {
		opacity: 0.7;
	}

	/* ---------- Stats Section ---------- */

	.stats-section {
		padding: 5rem 2rem;
		background-color: #fafaf7;
	}

	.stats-container {
		max-width: 800px;
		margin: 0 auto;
		display: flex;
		justify-content: center;
		gap: 5rem;
	}

	.stat {
		text-align: center;
	}

	.stat-number {
		font-family: 'Amiri', serif;
		font-size: 3rem;
		font-weight: 700;
		color: #2c2925;
		display: block;
		line-height: 1.2;
	}

	.stat-label {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.85rem;
		font-weight: 400;
		color: #6b6560;
		display: block;
		margin-top: 0.5rem;
	}

	/* ---------- About Preview ---------- */

	.about-section {
		padding: 6rem 2rem;
		background-color: #f2f0eb;
	}

	.about-container {
		max-width: 700px;
		margin: 0 auto;
		text-align: center;
	}

	.about-section .section-title {
		margin: 0 0 1.5rem;
	}

	.about-text {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 1.05rem;
		line-height: 2.2;
		color: #2c2925;
		margin: 2.5rem 0;
		text-align: justify;
		direction: rtl;
	}

	/* ---------- Footer ---------- */

	.footer {
		background-color: #1a1816;
		color: #ffffff;
		padding: 4rem 2rem;
	}

	.footer-inner {
		max-width: 800px;
		margin: 0 auto;
		text-align: center;
	}

	.footer-name {
		font-family: 'Amiri', serif;
		font-size: 1.5rem;
		font-weight: 700;
		color: #ffffff;
		margin: 0 0 0.75rem;
	}

	.footer-copy {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.85rem;
		font-weight: 300;
		color: rgba(255, 255, 255, 0.6);
		margin: 0 0 2rem;
	}

	.footer-nav {
		display: flex;
		justify-content: center;
		gap: 2.5rem;
		flex-wrap: wrap;
	}

	.footer-link {
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.85rem;
		font-weight: 400;
		color: rgba(255, 255, 255, 0.7);
		text-decoration: none;
		transition: color 0.2s ease;
		min-height: 44px;
		display: flex;
		align-items: center;
	}

	.footer-link:hover {
		color: #ffffff;
	}

	/* ---------- Responsive ---------- */

	@media (max-width: 1024px) {
		.hero-name {
			font-size: 3.5rem;
		}

		.stats-container {
			gap: 3rem;
		}
	}

	@media (max-width: 768px) {
		.page {
			font-size: 16px;
		}

		.nav-inner {
			padding: 1rem 1.5rem;
		}

		.nav-links {
			gap: 1.5rem;
		}

		.nav-link {
			font-size: 0.85rem;
		}

		.hero {
			padding: 4rem 1.5rem;
		}

		.hero-name {
			font-size: 2.8rem;
		}

		.hero-subtitle {
			font-size: 1rem;
		}

		.poems-grid {
			grid-template-columns: 1fr;
			gap: 1.5rem;
		}

		.section-title {
			font-size: 1.8rem;
		}

		.poems-section,
		.about-section {
			padding: 4rem 1.5rem;
		}

		.stats-container {
			gap: 2rem;
		}

		.stat-number {
			font-size: 2.2rem;
		}

		.verse-line {
			gap: 0.75rem;
		}

		.sadr,
		.ajz {
			font-size: 1rem;
		}
	}

	@media (max-width: 480px) {
		.nav-inner {
			padding: 0.75rem 1rem;
		}

		.nav-links {
			gap: 1rem;
		}

		.nav-logo {
			font-size: 1.25rem;
		}

		.hero-name {
			font-size: 2.2rem;
		}

		.hero-verse {
			margin: 2rem auto;
		}

		.verse-line {
			grid-template-columns: 1fr;
			gap: 0;
			text-align: center;
		}

		.verse-divider {
			display: none;
		}

		.sadr,
		.ajz {
			text-align: center;
		}

		.poem-card {
			padding: 1.75rem 1.25rem;
		}

		.stats-container {
			flex-direction: column;
			gap: 2rem;
		}

		.footer-nav {
			gap: 1.5rem;
		}

		.about-text {
			text-align: right;
		}
	}

	@media (max-width: 320px) {
		.hero-name {
			font-size: 1.8rem;
		}

		.nav-inner {
			gap: 0.75rem;
			flex-wrap: wrap;
			justify-content: center;
		}
	}
</style>
