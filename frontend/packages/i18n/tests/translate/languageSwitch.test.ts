import { mount } from "@vue/test-utils";
import { defineComponent, h, nextTick } from "vue";
import { describe, expect, it } from "vitest";

import { createI18n } from "../../src/translate/createI18n";
import { useI18n } from "../../src/translate/useI18n";

const catalogs = { en: { greeting: "Hello" }, fr: { greeting: "Bonjour" } };

const Greeting = defineComponent({
  setup() {
    const { t } = useI18n();
    return () => h("p", { id: "greeting" }, t("greeting"));
  },
});

describe("language switch", () => {
  it("shows the text in the first language", () => {
    const i18n = createI18n({ locale: "en-GB", catalogs });
    const wrapper = mount(Greeting, { global: { plugins: [i18n] } });
    expect(wrapper.get("#greeting").text()).toBe("Hello");
  });

  it("re-renders the same element in the new language", async () => {
    const i18n = createI18n({ locale: "en-GB", catalogs });
    const wrapper = mount(Greeting, { global: { plugins: [i18n] } });
    const node = wrapper.get("#greeting").element;
    i18n.setLocale("fr-FR");
    await nextTick();
    expect(wrapper.get("#greeting").element).toBe(node);
    expect(node.textContent).toBe("Bonjour");
  });

  it("does not reload the page when the language changes", async () => {
    const i18n = createI18n({ locale: "en-GB", catalogs });
    mount(Greeting, { global: { plugins: [i18n] } });
    const before = window.location.href;
    i18n.setLocale("fr-FR");
    await nextTick();
    expect(window.location.href).toBe(before);
  });

  it("shows the first language again when switching back", async () => {
    const i18n = createI18n({ locale: "en-GB", catalogs });
    const wrapper = mount(Greeting, { global: { plugins: [i18n] } });
    i18n.setLocale("fr-FR");
    await nextTick();
    i18n.setLocale("en-GB");
    await nextTick();
    expect(wrapper.get("#greeting").text()).toBe("Hello");
  });

  it("throws when the plugin is not installed", () => {
    expect(() => mount(Greeting)).toThrow(Error);
  });
});
