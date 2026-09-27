export function toArabicDigits(n: number | string): string {
	return String(n).replace(/\d/g, (d) => '٠١٢٣٤٥٦٧٨٩'[+d]);
}

/** Serialize an object as safe inline JSON-LD: escapes the `<` character so a
 *  value can never terminate the surrounding <script> element. */
export function jsonLd(obj: unknown): string {
	return JSON.stringify(obj).replace(/</g, '\\u003c');
}
