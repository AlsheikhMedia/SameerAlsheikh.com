export function toArabicDigits(n: number | string): string {
	return String(n).replace(/\d/g, (d) => '٠١٢٣٤٥٦٧٨٩'[+d]);
}
