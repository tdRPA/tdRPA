Chrome支持把浏览器Web UI元素当做native元素操作，从而可以通过Windows UIA自动化。只需要在启动Chrome时，加入参数 `--force-renderer-accessibility` 即可:
`"C:\Program Files\Google\Chrome\Application\chrome.exe" --force-renderer-accessibility`

技术说明见：https://www.chromium.org/developers/design-documents/accessibility