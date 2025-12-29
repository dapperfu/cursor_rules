# Plan: Create 10 Rust Development Rules

## Objective

Create 10 comprehensive Rust development rules following the same structure and quality standards as the existing Python, Makefile, and other rule sets. These rules SHALL be saved as `.mdc` files in a `rust/` directory and SHALL include Makefile targets for formatting and linting.

## TODO

1. [ ] Save this plan to the `plans/` folder (completed)
2. [ ] Gather answers to all questions below
3. [ ] Create `rust/` directory structure
4. [ ] Create rule for Rust toolchain version requirements
5. [ ] Create rule for Cargo.toml configuration standards
6. [ ] Create rule for Rust formatting (rustfmt) with Makefile target
7. [ ] Create rule for Rust linting (clippy) with Makefile target
8. [ ] Create rule for Rust documentation standards
9. [ ] Create rule for Rust error handling patterns
10. [ ] Create rule for Rust testing standards
11. [ ] Create rule for Rust dependency management
12. [ ] Create rule for Rust project structure
13. [ ] Create rule for Rust unsafe code usage
14. [ ] Create rule for Rust async/await patterns (if applicable)
15. [ ] Update README.md to include Rust rules section
16. [ ] Commit all changes to git

## Questions (Minimum 10 Required)

### Toolchain and Version Management

1. **Rust toolchain version**: What Rust toolchain version should be required? Should we mandate a minimum stable version (e.g., 1.70+), or allow nightly/stable flexibility? Should we use `rust-toolchain.toml` or `rust-toolchain` file?

2. **Toolchain management**: Should projects use `rustup` for toolchain management, and should we require a specific toolchain file format? Should we mandate `rust-toolchain.toml` over the older `rust-toolchain` file?

### Formatting and Linting

3. **Formatting tool**: Should we use `rustfmt` with default settings, or require specific configuration via `rustfmt.toml`? What formatting rules should be mandatory (e.g., line length, imports organization)?

4. **Linting tool**: Should we require `clippy` with default settings, or mandate specific clippy lints? Should we use `clippy.toml` for configuration? What clippy lint levels should be enforced (warn vs deny)?

5. **Makefile targets**: What should the Makefile targets be named? Should we follow the pattern `format` and `lint`, or use `rust-format` and `rust-lint`? Should these targets run automatically on certain operations?

6. **Pre-commit hooks**: Should formatting and linting be required to pass before commits, or just recommended? Should we include a Makefile target for pre-commit checks?

### Project Structure and Configuration

7. **Cargo.toml standards**: What metadata should be required in `Cargo.toml`? Should we mandate specific fields like `authors`, `license`, `edition`, `rust-version`? What Rust edition should be required (2021, 2024)?

8. **Project structure**: Should we require a specific project structure (e.g., `src/` directory, `tests/` directory, `examples/`)? Should we allow workspace projects, or focus on single-crate projects?

9. **Dependency management**: Should we require specific practices for dependency management? Should we mandate `Cargo.lock` for applications vs libraries? Should we require dependency version pinning or allow ranges?

### Code Quality and Standards

10. **Documentation**: What documentation standards should be enforced? Should we require rustdoc comments for all public items? Should we mandate specific documentation formats or examples?

11. **Error handling**: Should we require specific error handling patterns (e.g., `Result<T, E>`, custom error types, `anyhow`/`thiserror`)? Should we prohibit `unwrap()` and `expect()` in production code, or allow them with conditions?

12. **Unsafe code**: Should we have strict rules about `unsafe` code usage? Should `unsafe` blocks require documentation explaining why they're safe? Should we require audit trails for unsafe code?

13. **Testing**: What testing standards should be enforced? Should we require unit tests, integration tests, or both? Should we mandate test coverage thresholds? Should we require `#[cfg(test)]` organization?

14. **Async/await**: If the project uses async Rust, should we require specific async runtimes (tokio, async-std)? Should we mandate specific patterns for async error handling and cancellation?

15. **Type system usage**: Should we require specific type system practices? Should we mandate `#[derive]` usage patterns, or require explicit trait implementations in certain cases?

16. **Memory safety**: Should we have specific rules about ownership, borrowing, and lifetimes? Should we require explicit lifetime annotations in certain scenarios?

17. **Macros and code generation**: Should we have rules about macro usage? Should we require `macro_rules!` vs procedural macros? Should we mandate documentation for custom macros?

18. **Performance**: Should we require performance considerations? Should we mandate benchmarks for performance-critical code? Should we require specific profiling or optimization practices?

19. **Build and release**: Should we require specific Cargo profiles (dev, release)? Should we mandate optimization settings or debug symbol requirements?

20. **Integration with existing rules**: How should Rust rules integrate with existing Makefile, git, and safety rules? Should Rust-specific Makefile targets follow the same dependency patterns as Python targets?

## Scope and Constraints

- Rules SHALL follow the same `.mdc` format as existing rules
- Rules SHALL be atomic and focused (one rule per file)
- Rules SHALL include appropriate `globs` patterns for Rust files (`*.rs`, `Cargo.toml`, etc.)
- Makefile targets SHALL follow existing Makefile rule patterns (target dependencies, variable escaping)
- Rules SHALL use requirements language (SHALL, SHALL NOT, MUST, SHOULD)

## Deliverables

1. `rust/` directory with 10 `.mdc` rule files
2. Each rule file with proper frontmatter (description, globs, alwaysApply)
3. Makefile examples or targets for formatting and linting
4. Updated README.md documentation

## Success Criteria

- All 10 Rust rules created and follow project standards
- Makefile targets for `format` and `lint` are defined and documented
- Rules are properly scoped with globs patterns
- README.md updated to include Rust rules section
- All files committed to git with proper commit message







