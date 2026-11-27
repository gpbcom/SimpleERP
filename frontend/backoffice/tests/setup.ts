import { afterEach, beforeEach } from "vitest";

import { installMatchMedia } from "./helpers/media";
import type { MediaController } from "./helpers/media";

let media: MediaController | undefined;

beforeEach(() => {
  if (typeof window === "undefined") {
    return;
  }
  media = installMatchMedia({ widthPx: 1280, dark: false });
});

afterEach(() => {
  media?.uninstall();
  media = undefined;
  if (typeof localStorage !== "undefined") {
    localStorage.clear();
  }
  if (typeof document === "undefined") {
    return;
  }
  const root = document.documentElement;
  root.removeAttribute("data-theme");
  root.removeAttribute("lang");
  root.style.colorScheme = "";
  document.body.innerHTML = "";
});
