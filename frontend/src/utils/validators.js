export function isValidText(text) {
  return text && text.trim().length > 0 && text.length <= 5000;
}
