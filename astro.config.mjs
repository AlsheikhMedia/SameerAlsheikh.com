import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
	site: 'https://sameeralsheikh.com',
	output: 'static',
	trailingSlash: 'always',
	build: {
		inlineStylesheets: 'always',
	},
	prefetch: {
		prefetchAll: true,
		defaultStrategy: 'hover',
	},
	integrations: [sitemap()],
});
