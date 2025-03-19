Creating an ebook from SLIME MOLD TIME MOLD's excellent series, The Mind in the Wheel.

https://slimemoldtimemold.com/tag/the-mind-in-the-wheel/

Using Standard Ebooks awesome tools: https://github.com/standardebooks/tools

And messily following their [standards](https://standardebooks.org/manual/1.8.1/) and [step by step guide](https://standardebooks.org/contribute/producing-an-ebook-step-by-step)

steps for image clean up
1. `/<img` to search for them all
2. `v` and up to delete the from figure and div
3. Macro: `qa%c$/>ESCq` to clean up the end. Then just do `@a` from the start of the img tag
4. For captions, same `v` step, then manually do `%i/` and tap over to drop the figcaption to a new line
5. clean up the fig capture end with `$bbbd$`. some number of b's to get through the the figure and div
6. To do the subchapters, crip the `h3` formatting from others. Have to close sections and update wp class to epub type

Build steps:
- `se build .`
- `se typogrify .` (maybe not?)
- `se semanticate .`
- `se find-mismatched-dashes .`
- `se build-title .`
- `se build-manifest .`
- `se build-spine .`
- `se build-toc .`
- `se clean .`
- `se lint .` (not working)

TODO:
- Wire up images
- Put build steps in script
- fix lints, lots there whew
- Clean up the colophon pages for actual publish, it's not a fully supprted standard ebook, just do a blurb thanking?
- actually label everything?
- Try to pull it into a submodule, might be too late
- Remove the junk images up above, can just do it in the history though as I wire up images
