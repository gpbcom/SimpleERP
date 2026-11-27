/** The two colour themes of the design system. */
export type ThemeName = "light" | "dark";

/** The three font roles of the design system. */
export type FontRole = "heading" | "body" | "code";

/** A value that differs between the light and the dark theme. */
export interface ThemedValue {
  /** The value in the light theme. */
  light: string;
  /** The value in the dark theme. */
  dark: string;
}

/** A size that differs between the comfortable and the compact density, in pixels. */
export interface DensityValue {
  /** The size in the comfortable density. */
  comfortable: number;
  /** The size in the compact density. */
  compact: number;
}

/** One typographic style. */
export interface TypeStyle {
  /** The font role the style uses. */
  family: FontRole;
  /** The font size in pixels. */
  sizePx: number;
  /** The line height in pixels. */
  lineHeightPx: number;
  /** The font weight. */
  weight: number;
}

/** One font file served by the package. */
export interface FontFile {
  /** The font family name. */
  family: string;
  /** The font weight of the file. */
  weight: number;
  /** The file name, under the package's fonts folder. */
  file: string;
  /** The npm package the file comes from. */
  package: string;
}

/** Everything the design tokens are generated from. */
export interface TokenSource {
  /** The colours, by token name, in both themes. */
  colors: Record<string, ThemedValue>;
  /** The spacing scale, in pixels. */
  spacing: number[];
  /** The sizes that change with the density, by token name. */
  density: Record<string, DensityValue>;
  /** The font families by role, and the typographic styles by name. */
  typography: {
    families: Record<FontRole, string>;
    styles: Record<string, TypeStyle>;
  };
  /** The corner radii, by token name. */
  radius: Record<string, string>;
  /** The shadows, by token name, in both themes. */
  elevation: Record<string, ThemedValue>;
  /** The font files to serve. */
  fonts: FontFile[];
}
