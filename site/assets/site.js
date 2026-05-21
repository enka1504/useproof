const nav = document.querySelector('.nav');
const toggle = document.querySelector('[data-menu-toggle]');

if (toggle && nav) {
	toggle.addEventListener('click', () => {
		nav.classList.toggle('open');
	});
}

const tabs = document.querySelectorAll('[data-tab]');
const panels = document.querySelectorAll('[data-tab-panel]');

tabs.forEach((button) => {
	button.addEventListener('click', () => {
		const target = button.dataset.tab;
		tabs.forEach((tab) => tab.classList.toggle('active', tab === button));
		panels.forEach((panel) => panel.classList.toggle('active', panel.dataset.tabPanel === target));
	});
});

const copyButtons = document.querySelectorAll('[data-copy]');

copyButtons.forEach((button) => {
	button.addEventListener('click', async () => {
		const selector = button.dataset.copy;
		const target = selector ? document.querySelector(selector) : null;
		if (!target) return;

		const text = target.textContent.trim();
		try {
			await navigator.clipboard.writeText(text);
			const original = button.textContent;
			button.textContent = 'Copied';
			window.setTimeout(() => {
				button.textContent = original;
			}, 1300);
		} catch {
			button.textContent = 'Select text';
		}
	});
});
