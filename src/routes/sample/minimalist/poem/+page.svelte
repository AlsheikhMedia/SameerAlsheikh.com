<script lang="ts">
	import { samplePoems, categories } from '$lib/utils/poems';

	const poem = samplePoems[0]; // قصيدة الوطن — longest poem
	const nextPoem = samplePoems[1]; // Suggested next poem

	// Convert Western digits to Eastern Arabic digits
	function toArabicDigits(n: number | string): string {
		return String(n).replace(/\d/g, (d) => '٠١٢٣٤٥٦٧٨٩'[+d]);
	}

	// Font size control
	let fontSizeLevel = $state(1); // 0=small, 1=default, 2=large, 3=xlarge
	const fontSizes = [
		{ verse: '1.05rem', lineHeight: '2.2' },
		{ verse: '1.25rem', lineHeight: '2.4' },
		{ verse: '1.5rem',  lineHeight: '2.6' },
		{ verse: '1.75rem', lineHeight: '2.8' },
	];

	function decreaseFont() {
		if (fontSizeLevel > 0) fontSizeLevel--;
	}
	function increaseFont() {
		if (fontSizeLevel < 3) fontSizeLevel++;
	}

	// Controls toggle
	let controlsOpen = $state(false);
	let shareOpen = $state(false);

	// Font family control
	const fontChoices = [
		{ id: 'amiri', family: "'Amiri', serif", label: 'الأميري', sample: 'نسخ كلاسيكي' },
		{ id: 'noto', family: "'Noto Naskh Arabic', serif", label: 'النسخ', sample: 'نسخ عصري' },
		{ id: 'ruqaa', family: "'Aref Ruqaa', serif", label: 'الرقعة', sample: 'خط الرقعة' },
		{ id: 'cairo', family: "'Cairo', sans-serif", label: 'القاهرة', sample: 'خط عصري' },
	];
	let activeFontIndex = $state(0);

	// Reading bookmark
	import { onMount } from 'svelte';

	const bookmarkKey = `bookmark-${poem.slug}`;
	let bookmarkedLine = $state<number | null>(null);

	onMount(() => {
		const saved = localStorage.getItem(bookmarkKey);
		if (saved !== null) {
			bookmarkedLine = parseInt(saved, 10);
			// Scroll to bookmarked line after a brief delay for render
			setTimeout(() => {
				const el = document.getElementById(`verse-${bookmarkedLine}`);
				if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}, 300);
		}
	});

	function toggleBookmark(index: number) {
		if (bookmarkedLine === index) {
			bookmarkedLine = null;
			localStorage.removeItem(bookmarkKey);
		} else {
			bookmarkedLine = index;
			localStorage.setItem(bookmarkKey, String(index));
		}
	}

	// Share functionality
	const shareText = `${poem.title} — سمير الشيخ حسين\n\n${poem.verses[0].sadr}    ${poem.verses[0].ajz}`;

	function getShareUrl() {
		if (typeof window !== 'undefined') return window.location.href;
		return '';
	}

	function shareWhatsApp() {
		const url = `https://wa.me/?text=${encodeURIComponent(shareText + '\n\n' + getShareUrl())}`;
		window.open(url, '_blank', 'noopener');
	}

	function shareTelegram() {
		const url = `https://t.me/share/url?url=${encodeURIComponent(getShareUrl())}&text=${encodeURIComponent(shareText)}`;
		window.open(url, '_blank', 'noopener');
	}

	function shareX() {
		const url = `https://x.com/intent/tweet?text=${encodeURIComponent(shareText)}&url=${encodeURIComponent(getShareUrl())}`;
		window.open(url, '_blank', 'noopener');
	}

	function shareFacebook() {
		const url = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(getShareUrl())}`;
		window.open(url, '_blank', 'noopener');
	}

	function shareEmail() {
		const subject = encodeURIComponent(`${poem.title} — سمير الشيخ`);
		const body = encodeURIComponent(shareText + '\n\n' + getShareUrl());
		window.location.href = `mailto:?subject=${subject}&body=${body}`;
	}

	let copySuccess = $state(false);
	function copyLink() {
		navigator.clipboard.writeText(getShareUrl()).then(() => {
			copySuccess = true;
			setTimeout(() => copySuccess = false, 2000);
		});
	}
</script>

<svelte:head>
	<title>{poem.title} — سمير الشيخ حسين</title>
</svelte:head>

<div class="page" dir="rtl" lang="ar">
	<!-- Navigation -->
	<nav class="nav">
		<div class="nav-inner">
			<a href="/sample/minimalist" class="nav-logo">سمير الشيخ حسين</a>
			<div class="nav-links">
				<a href="/sample/minimalist#poems" class="nav-link active">الديوان</a>
				<a href="/sample/minimalist#about" class="nav-link">عن الشاعر</a>
				<a href="/sample/minimalist#contact" class="nav-link">تواصل</a>
			</div>
		</div>
	</nav>

	<!-- Poem Page -->
	<main class="poem-page">
		<!-- Breadcrumb -->
		<div class="breadcrumb">
			<a href="/sample/minimalist">الرئيسية</a>
			<span class="sep">/</span>
			<a href="/sample/minimalist#poems">الديوان</a>
			<span class="sep">/</span>
			<span class="current">{poem.title}</span>
		</div>

		<!-- Poem Header -->
		<header class="poem-header">
			<div class="rule"></div>
			<h1 class="poem-title">{poem.title}</h1>

			<div class="poem-meta">
				<span class="meta-item">
					<span class="meta-label">البحر:</span>
					<a href="/sample/minimalist?meter={encodeURIComponent(poem.meter)}" class="meta-tag">{poem.meter}</a>
				</span>
				<span class="meta-divider"></span>
				<span class="meta-item">
					<span class="meta-label">الباب:</span>
					<a href="/sample/minimalist?category={poem.category}" class="meta-tag">{categories[poem.category]}</a>
				</span>
				{#if poem.date}
					<span class="meta-divider"></span>
					<span class="meta-item">
						<span class="meta-label">التاريخ:</span>
						{new Date(poem.date).toLocaleDateString('ar-SA', { year: 'numeric', month: 'long', day: 'numeric' })}
					</span>
				{/if}
			</div>

			<div class="rule"></div>
		</header>

		<!-- Toolbar: Font + Share toggles -->
		<div class="toolbar-wrap no-print">
			<div class="toolbar-buttons">
				<button
					class="toolbar-circle-btn"
					class:toolbar-circle-open={controlsOpen}
					onclick={() => { controlsOpen = !controlsOpen; if (controlsOpen) shareOpen = false; }}
					aria-expanded={controlsOpen}
					aria-controls="font-controls"
					aria-label="إعدادات الخط"
				>
					<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
						<path d="M17 3a2.828 2.828 0 114 4L7.5 20.5 2 22l1.5-5.5L17 3z"/>
						<path d="M15 5l4 4"/>
					</svg>
				</button>
				<button
					class="toolbar-circle-btn"
					class:toolbar-circle-open={shareOpen}
					onclick={() => { shareOpen = !shareOpen; if (shareOpen) controlsOpen = false; }}
					aria-expanded={shareOpen}
					aria-controls="share-controls"
					aria-label="مشاركة القصيدة"
				>
					<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
						<circle cx="18" cy="5" r="3"/>
						<circle cx="6" cy="12" r="3"/>
						<circle cx="18" cy="19" r="3"/>
						<line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
						<line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
					</svg>
				</button>
			</div>

			<div id="font-controls" class="font-controls" class:font-controls-open={controlsOpen}>
				<div class="font-controls-inner">
					<div class="size-buttons">
						<button
							onclick={increaseFont}
							disabled={fontSizeLevel === 3}
							aria-label="تكبير الخط"
							class="size-btn"
						>&plus;</button>
						<button
							onclick={decreaseFont}
							disabled={fontSizeLevel === 0}
							aria-label="تصغير الخط"
							class="size-btn"
						>&minus;</button>
					</div>
					<div class="font-choices">
						{#each fontChoices as font, i}
							<button
								class="font-choice"
								class:font-choice-active={activeFontIndex === i}
								style="font-family: {font.family};"
								onclick={() => activeFontIndex = i}
								aria-label="خط {font.label}"
								aria-pressed={activeFontIndex === i}
							>
								<span class="font-choice-name">{font.label}</span>
								<span class="font-choice-sample">{font.sample}</span>
							</button>
						{/each}
					</div>
				</div>
			</div>

			<div id="share-controls" class="font-controls" class:font-controls-open={shareOpen}>
				<div class="font-controls-inner" role="group" aria-label="مشاركة القصيدة">
					<button onclick={shareWhatsApp} class="share-btn" aria-label="مشاركة عبر واتساب">
						<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
							<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
						</svg>
					</button>
					<button onclick={shareTelegram} class="share-btn" aria-label="مشاركة عبر تيليجرام">
						<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
							<path d="M11.944 0A12 12 0 000 12a12 12 0 0012 12 12 12 0 0012-12A12 12 0 0012 0a12 12 0 00-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 01.171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.479.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
						</svg>
					</button>
					<button onclick={shareX} class="share-btn" aria-label="مشاركة عبر إكس">
						<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
							<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
						</svg>
					</button>
					<button onclick={shareFacebook} class="share-btn" aria-label="مشاركة عبر فيسبوك">
						<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
							<path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
						</svg>
					</button>
					<button onclick={shareEmail} class="share-btn" aria-label="مشاركة عبر البريد الإلكتروني">
						<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
							<rect x="2" y="4" width="20" height="16" rx="2"/>
							<path d="M22 4L12 13 2 4"/>
						</svg>
					</button>
					<button onclick={copyLink} class="share-btn" aria-label="نسخ الرابط">
						{#if copySuccess}
							<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
								<polyline points="20 6 9 17 4 12"/>
							</svg>
						{:else}
							<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
								<path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/>
								<path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/>
							</svg>
						{/if}
					</button>
				</div>
			</div>
		</div>

		<!-- Poem Body: The Verses -->
		<article class="poem-body">
			{#each poem.verses as verse, i}
				<div
					id="verse-{i}"
					class="verse-row"
					class:verse-bookmarked={bookmarkedLine === i}
					style="font-size: {fontSizes[fontSizeLevel].verse}; line-height: {fontSizes[fontSizeLevel].lineHeight}; --verse-font: {fontChoices[activeFontIndex].family};"
					onclick={() => toggleBookmark(i)}
					role="button"
					tabindex="0"
					onkeydown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleBookmark(i); }}}
					aria-label="البيت {toArabicDigits(i + 1)} — اضغط لتعليم موضع القراءة"
					aria-pressed={bookmarkedLine === i}
				>
					<span class="verse-number">{toArabicDigits(i + 1)}</span>
					<span class="sadr">{verse.sadr}</span>
					<span class="verse-divider" aria-hidden="true"></span>
					<span class="ajz">{verse.ajz}</span>
				</div>
			{/each}
		</article>

		<hr class="poem-end-rule" />

		<!-- Navigation + Footer -->
		<nav class="poem-nav no-print" aria-label="التنقل بين القصائد">
			<a href="/sample/minimalist" class="back-link">
				<span class="arrow" aria-hidden="true">&rarr;</span>
				العودة إلى الديوان
			</a>
			<div class="nav-footer">
				<p class="nav-footer-name">سمير الشيخ حسين</p>
				<p class="nav-footer-copy">جميع الحقوق محفوظة ٢٠٢٦</p>
			</div>
			<a href="#" class="nav-link-btn">
				{nextPoem.title}
				<span class="arrow" aria-hidden="true">&larr;</span>
			</a>
		</nav>
	</main>
</div>

<style>
	/* ============================================
	   Full Poem Page - Minimalist Style
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
		zoom: 1.25;
		min-height: 100vh;
		display: flex;
		flex-direction: column;
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
		font-size: 2rem;
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

	.nav-link:hover { color: #7a2532; }
	.nav-link.active::after { transform: scaleX(1); }
	.nav-link.active { color: #7a2532; }

	/* ---------- Rule ---------- */

	.rule {
		width: 80px;
		height: 2px;
		background-color: #7a2532;
		margin: 0 auto;
	}

	/* ---------- Poem Page ---------- */

	.poem-page {
		flex: 1;
		max-width: 900px;
		width: 100%;
		margin: 0 auto;
		padding: 2rem 2rem 4rem;
	}

	/* ---------- Breadcrumb ---------- */

	.breadcrumb {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		font-size: 0.85rem;
		color: #6b6560;
		margin-bottom: 3rem;
		padding-top: 1rem;
	}

	.breadcrumb a {
		color: #6b6560;
		text-decoration: none;
		transition: color 0.2s;
		min-height: 44px;
		display: inline-flex;
		align-items: center;
	}

	.breadcrumb a:hover { color: #7a2532; }

	.breadcrumb .sep {
		opacity: 0.4;
		font-size: 0.75rem;
	}

	.breadcrumb .current {
		color: #2c2925;
		font-weight: 500;
	}

	/* ---------- Poem Header ---------- */

	.poem-header {
		text-align: center;
		margin-bottom: 2rem;
	}

	.poem-title {
		font-family: 'Amiri', serif;
		font-size: 2.4rem;
		font-weight: 700;
		color: #2c2925;
		margin: 2rem 0 1.5rem;
		line-height: 1.3;
	}

	.poem-meta {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 1.25rem;
		font-size: 0.9rem;
		color: #6b6560;
		margin-bottom: 2rem;
		flex-wrap: wrap;
	}

	.meta-label {
		font-weight: 500;
		color: #2c2925;
	}

	.meta-divider {
		width: 4px;
		height: 4px;
		border-radius: 50%;
		background-color: #d0cdc8;
	}

	.meta-tag {
		color: #7a2532;
		text-decoration: none;
		font-weight: 500;
	}

	/* ---------- Toolbar (Font + Share toggles) ---------- */

	.toolbar-wrap {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 2.5rem;
	}

	.toolbar-buttons {
		display: flex;
		gap: 0.75rem;
	}

	.toolbar-circle-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 44px;
		height: 44px;
		border: 1px solid #d0cdc8;
		border-radius: 50%;
		background: #fafaf7;
		color: #6b6560;
		cursor: pointer;
		transition: border-color 0.2s, color 0.2s, background-color 0.2s;
	}

	.toolbar-circle-btn:hover,
	.toolbar-circle-open {
		border-color: #7a2532;
		color: #7a2532;
		background-color: rgba(122, 37, 50, 0.04);
	}

	/* ---------- Collapsible Font Controls ---------- */

	.font-controls {
		display: grid;
		grid-template-rows: 0fr;
		transition: grid-template-rows 0.3s ease;
		overflow: hidden;
	}

	.font-controls-open {
		grid-template-rows: 1fr;
	}

	.font-controls-inner {
		min-height: 0;
		display: flex;
		justify-content: center;
		gap: 0.375rem;
		padding-top: 0;
		transition: padding-top 0.3s ease;
	}

	.font-controls-open .font-controls-inner {
		padding-top: 1rem;
	}

	.size-buttons {
		display: flex;
		flex-direction: column;
		gap: 0.375rem;
	}

	.size-btn {
		font-size: 1.1rem;
		font-weight: 700;
		color: #2c2925;
		background: none;
		border: 1px solid #d0cdc8;
		border-radius: 4px;
		width: 44px;
		flex: 1;
		cursor: pointer;
		transition: border-color 0.2s, color 0.2s;
		display: flex;
		align-items: center;
		justify-content: center;
		line-height: 1;
	}

	.size-btn:hover:not(:disabled) {
		border-color: #7a2532;
		color: #7a2532;
	}

	.size-btn:disabled {
		opacity: 0.3;
		cursor: not-allowed;
	}

	.font-choices {
		display: flex;
		gap: 0.375rem;
	}

	.font-choice {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 64px;
		width: 80px;
		border: 1px solid #d0cdc8;
		border-radius: 4px;
		background: #fafaf7;
		cursor: pointer;
		transition: border-color 0.2s, background-color 0.2s;
	}

	.font-choice:hover {
		border-color: #7a2532;
	}

	.font-choice-active {
		border-color: #7a2532;
		background-color: #fff;
		box-shadow: 0 0 0 1px #7a2532;
	}

	.font-choice-name {
		font-size: 0.95rem;
		font-weight: 700;
		color: #2c2925;
		line-height: 1.3;
	}

	.font-choice-sample {
		font-size: 0.65rem;
		color: #8a847d;
		font-family: 'IBM Plex Sans Arabic', sans-serif !important;
		font-weight: 400;
	}

	/* =============================================
	   VERSE LAYOUT — Two-Hemistich (صدر | عجز)

	   The core Arabic poetry alignment:
	   - Each بيت is a row with a verse number + content area
	   - Content area is a 3-column grid: صدر | divider | عجز
	   - Both hemistichs have equal width columns
	   - Text is CENTER-aligned within each column
	   - This creates the classic mirrored layout around
	     the central axis, just like a printed ديوان
	   ============================================= */

	.poem-body {
		margin: 0 auto;
		max-width: 800px;
	}

	.verse-row {
		position: relative;
		display: grid;
		grid-template-columns: 1fr auto 1fr;
		align-items: baseline;
		gap: 2rem;
		padding: 0.6rem 0;
		border-bottom: 1px solid transparent;
		transition: border-color 0.2s, background-color 0.2s;
		font-family: var(--verse-font, 'Amiri', serif);
	}

	.verse-row:hover {
		background-color: rgba(122, 37, 50, 0.02);
		border-bottom-color: #eae7e2;
		cursor: pointer;
	}

	.verse-bookmarked {
		background-color: rgba(122, 37, 50, 0.05);
		border-bottom-color: #e0ddd8;
	}

	.verse-number {
		position: absolute;
		right: -2.5rem;
		top: 50%;
		transform: translateY(-50%);
		font-family: 'IBM Plex Sans Arabic', sans-serif;
		font-size: 0.7rem;
		color: #b5b0a8;
		user-select: none;
		width: 1.5rem;
		height: 1.5rem;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
		transition: background-color 0.2s, color 0.2s;
	}

	.verse-bookmarked .verse-number {
		background-color: #7a2532;
		color: #fff;
	}

	.sadr {
		text-align: center;
	}

	.ajz {
		text-align: center;
	}

	.verse-divider {
		width: 1px;
		align-self: stretch;
		min-height: 1.5em;
		background-color: #7a2532;
		opacity: 0.25;
	}

	/* ---------- Poem End Rule ---------- */

	.poem-end-rule {
		border: none;
		border-top: 1px solid #e0ddd8;
		margin: 3rem auto 1.5rem;
	}

	.share-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 44px;
		height: 44px;
		border: 1px solid #d0cdc8;
		border-radius: 4px;
		background: none;
		color: #6b6560;
		cursor: pointer;
		transition: border-color 0.2s, color 0.2s, background-color 0.2s;
	}

	.share-btn:hover {
		border-color: #7a2532;
		color: #7a2532;
		background-color: rgba(122, 37, 50, 0.04);
	}

	/* ---------- Poem Navigation ---------- */

	.poem-nav {
		margin-top: 1.25rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.back-link,
	.nav-link-btn {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		font-size: 0.95rem;
		font-weight: 500;
		color: #7a2532;
		text-decoration: none;
		min-height: 44px;
		transition: gap 0.2s;
	}

	.back-link:hover,
	.nav-link-btn:hover {
		gap: 0.75rem;
	}

	.arrow {
		font-size: 1.2rem;
		line-height: 1;
	}

	/* ---------- Nav Footer (inline) ---------- */

	.nav-footer {
		text-align: center;
	}

	.nav-footer-name {
		font-family: 'Amiri', serif;
		font-size: 1rem;
		font-weight: 700;
		color: #2c2925;
		margin: 0;
		line-height: 1.4;
	}

	.nav-footer-copy {
		font-size: 0.7rem;
		font-weight: 300;
		color: #8a847d;
		margin: 0;
	}

	/* ---------- Responsive ---------- */

	@media (max-width: 768px) {
		.nav-inner {
			padding: 1rem 1.5rem;
		}

		.nav-links {
			gap: 1.5rem;
		}

		.poem-page {
			padding: 1.5rem 1.5rem 3rem;
		}

		.poem-title {
			font-size: 2.2rem;
		}

		.poem-meta {
			gap: 0.75rem;
			font-size: 0.85rem;
		}

		.verse-row {
			gap: 1rem;
		}

		.poem-nav {
			flex-wrap: wrap;
			justify-content: center;
			gap: 1rem;
		}

		.nav-footer {
			order: 3;
			width: 100%;
		}

		.nav-link-btn {
			justify-content: flex-end;
		}
	}

	/*
	   MOBILE STACKED LAYOUT
	   On narrow screens, hemistichs stack vertically.
	   The عجز gets a right-indent to visually distinguish it
	   from the صدر — a convention used in many Arabic poetry apps.
	*/
	@media (max-width: 520px) {
		.nav-inner {
			padding: 0.75rem 1rem;
		}

		.nav-links {
			gap: 1rem;
		}

		.nav-logo {
			font-size: 1.25rem;
		}

		.poem-page {
			padding: 1rem 1rem 2rem;
		}

		.poem-title {
			font-size: 1.8rem;
		}

		.breadcrumb {
			margin-bottom: 2rem;
		}

		.verse-row {
			gap: 0.5rem;
		}

		.verse-row {
			grid-template-columns: 1fr;
			gap: 0;
		}

		.verse-number {
			position: static;
			transform: none;
			text-align: center;
			margin-bottom: 0.25rem;
		}

		.sadr {
			text-align: right;
			padding-bottom: 0.5em;
		}

		.ajz {
			text-align: left;
			padding-right: 0;
			padding-bottom: 0.5em;
			color: #3d3832;
		}

		.verse-divider {
			display: none;
		}

		.font-choices {
			gap: 0.25rem;
		}

		.font-choice {
			padding: 0.4rem 0.6rem;
			min-height: 56px;
		}
	}

	/* ---------- Print ---------- */

	@media print {
		.nav, .toolbar-wrap, .poem-nav, .breadcrumb {
			display: none !important;
		}

		.page {
			background: white;
			color: black;
		}

		.poem-page {
			padding: 0;
			max-width: 100%;
		}

		.verse-row:hover {
			background-color: transparent;
			border-bottom-color: transparent;
		}

		.verse-number {
			color: #999;
		}

		.verse-divider {
			background-color: #999;
			opacity: 1;
		}

		.verse-row {
			gap: 1.5rem;
		}
	}

	/* ---------- Reduced motion ---------- */

	@media (prefers-reduced-motion: reduce) {
		.font-controls {
			transition: none;
		}
		.font-controls-inner {
			transition: none;
		}
		.verse-row {
			transition: none;
		}
		.back-link {
			transition: none;
		}
	}
</style>
