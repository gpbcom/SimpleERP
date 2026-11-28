import { mount } from "@vue/test-utils";
import { defineComponent, h, nextTick } from "vue";
import { describe, expect, it } from "vitest";

import en from "../../src/catalogues/en/errors.json";
import fr from "../../src/catalogues/fr/errors.json";
import { ERROR_COMMON_KEYS, errorCatalog } from "../../src/errors/errorCatalog";
import { createI18n } from "../../src/translate/createI18n";
import { useI18n } from "../../src/translate/useI18n";
import type { Catalogs } from "../../src/types";

const catalogs: Catalogs = { en, fr };
const languages = ["en", "fr"] as const;
const entries = Object.entries(errorCatalog);
const fallbackKeys = ["errors.fallback.title", "errors.fallback.why", "errors.fallback.action"];
const commonKeys = [...ERROR_COMMON_KEYS];
const whyKeys = [...entries.map(([, entry]) => entry.whyKey), "errors.fallback.why"];
const messageKeys = [
  ...entries.flatMap(([, entry]) => [entry.titleKey, entry.whyKey, entry.actionKey]),
  ...fallbackKeys,
  ...commonKeys,
];

function translatorFor(language: string) {
  return createI18n({ locale: language, catalogs });
}

function placeholders(text: string): string[] {
  return [...text.matchAll(/\{(\w+)\}/g)].map((match) => match[1] as string).sort();
}

describe("error texts", () => {
  it("lists the keys of the common labels", () => {
    expect(commonKeys).toEqual(expect.arrayContaining(["errors.common.cancel", "errors.common.reference"]));
  });

  describe.each(languages)("in %s", (language) => {
    it("has a non-empty text for every key of the catalogue, the fallback and the common labels", () => {
      const { t } = translatorFor(language);
      const missing = messageKeys.filter((key) => {
        const text = t(key);
        return text === key || text.trim() === "";
      });
      expect(missing).toEqual([]);
    });

    it("never shows the error code or the support reference in a message", () => {
      const { t } = translatorFor(language);
      const offending = entries.flatMap(([code, entry]) =>
        [entry.titleKey, entry.whyKey, entry.actionKey]
          .filter((key) => {
            const text = t(key);
            return text.includes(code) || (entry.reference ? text.includes(entry.reference) : false);
          })
          .map((key) => `${code}: ${key}`),
      );
      expect(offending).toEqual([]);
    });

    it("writes every why text as one sentence ending with a full stop", () => {
      const { t } = translatorFor(language);
      const offending = whyKeys.filter((key) => {
        const text = t(key).trim();
        const body = text.slice(0, -1);
        return !text.endsWith(".") || /[.!?]\s/.test(body) || /[.!?]$/.test(body);
      });
      expect(offending).toEqual([]);
    });

    it("interpolates the placeholder of a why text with the value given", () => {
      const { t } = translatorFor(language);
      for (const key of whyKeys) {
        const names = placeholders(t(key));
        const params = Object.fromEntries(names.map((name) => [name, `value-of-${name}`]));
        const text = t(key, params);
        expect(text).not.toMatch(/\{\w+\}/);
        for (const name of names) {
          expect(text).toContain(`value-of-${name}`);
        }
      }
    });
  });

  it("keeps the same placeholders in both languages for every why text", () => {
    const english = translatorFor("en");
    const french = translatorFor("fr");
    for (const key of whyKeys) {
      expect(placeholders(french.t(key))).toEqual(placeholders(english.t(key)));
    }
  });

  it("changes the title text without a reload when the language switches", async () => {
    const i18n = translatorFor("en-GB");
    const titleKey = entries[0]?.[1].titleKey ?? "errors.fallback.title";
    const Title = defineComponent({
      setup() {
        const { t } = useI18n();
        return () => h("h1", { id: "title" }, t(titleKey));
      },
    });
    const wrapper = mount(Title, { global: { plugins: [i18n] } });
    const before = window.location.href;
    const english = wrapper.get("#title").text();
    i18n.setLocale("fr-FR");
    await nextTick();
    expect(wrapper.get("#title").text()).not.toBe(english);
    expect(wrapper.get("#title").text()).toBe(translatorFor("fr").t(titleKey));
    expect(window.location.href).toBe(before);
  });
});
