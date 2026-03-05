<svelte:head>
	<title>سمير الشيخ - اختيار التصميم</title>
</svelte:head>

<div class="chooser">
	<h1>سمير الشيخ</h1>
	<p class="subtitle">اختر التصميم المفضّل للموقع</p>

	<div class="cards">
		<a href="/sample/classical" class="card classical">
			<div class="card-icon">&#xFDFD;</div>
			<h2>المخطوطة الكلاسيكية</h2>
			<p>تصميم يستلهم المخطوطات العربية القديمة والدواوين المُذهَّبة. ألوان دافئة وزخارف إسلامية.</p>
		</a>

		<a href="/sample/minimalist" class="card minimalist">
			<div class="card-icon">&mdash;</div>
			<h2>الأناقة المعاصرة</h2>
			<p>تصميم عصري أنيق يعتمد البساطة والمساحات البيضاء. الشعر يتحدث عن نفسه.</p>
		</a>

		<a href="/sample/desert" class="card desert">
			<div class="card-icon">&#9788;</div>
			<h2>تراث الصحراء</h2>
			<p>تصميم مستوحى من الصحراء العربية وتراث البادية. رمال ذهبية وسماء ليلية.</p>
		</a>
	</div>
</div>

<style>
	.chooser {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 2rem;
		background: #1A1816;
		color: #F5ECD7;
		font-family: 'Amiri', serif;
	}

	h1 {
		font-family: 'Aref Ruqaa', serif;
		font-size: 3rem;
		margin-bottom: 0.5rem;
	}

	.subtitle {
		font-size: 1.2rem;
		opacity: 0.7;
		margin-bottom: 3rem;
	}

	.cards {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
		gap: 2rem;
		max-width: 1000px;
		width: 100%;
	}

	.card {
		display: block;
		padding: 2.5rem 2rem;
		border-radius: 8px;
		text-align: center;
		transition: transform 0.3s ease, box-shadow 0.3s ease;
		min-height: 44px;
	}

	.card:hover {
		transform: translateY(-4px);
		box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
	}

	.card-icon {
		font-size: 2.5rem;
		margin-bottom: 1rem;
	}

	.card h2 {
		font-family: 'Aref Ruqaa', serif;
		font-size: 1.5rem;
		margin-bottom: 0.75rem;
	}

	.card p {
		font-size: 0.95rem;
		line-height: 1.8;
		opacity: 0.85;
	}

	.classical {
		background: #2C1810;
		color: #F5ECD7;
		border: 2px solid #B8860B;
	}

	.minimalist {
		background: #FAFAF7;
		color: #2C2925;
		border: 2px solid #7A2532;
	}

	.desert {
		background: #2C1810;
		color: #F5EDE0;
		border: 2px solid #C4883A;
	}

	@media (max-width: 640px) {
		h1 { font-size: 2.2rem; }
		.cards { grid-template-columns: 1fr; }
	}
</style>
