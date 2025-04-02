## 安装依赖命令：

`./.venv/bin/python -m pip install beautifulsoup4 colorama termcolor readchar requests`
**安装异步协程爬取依赖命令：**
`./.venv/bin/python -m pip install asyncio aiohttp`
一般来说使用 `pip install ...` 命令即可

## 运行 python 文件命令

`python crawlingNovels.py`

## pip install 命令和./.venv/bin/python -m pip install 命令的异同

### 1. **功能**

- **`pip install`**：这是安装 Python 包的常用命令。它会根据当前的 Python 环境（全局环境或虚拟环境）来安装包。
- **`./.venv/bin/python -m pip install`**：这个命令明确地使用虚拟环境中的 Python 解释器来调用`pip`进行安装。它确保包被安装到指定的虚拟环境中，而不是全局环境中。

### 2. **使用场景**

- **`pip install`**：
  - 适用于全局环境或已激活的虚拟环境。
  - 如果虚拟环境未激活，包将安装到全局环境中。
  - 如果虚拟环境已激活，包将安装到虚拟环境中。
- **`./.venv/bin/python -m pip install`**：
  - 适用于未激活虚拟环境的场景。
  - 明确指定使用虚拟环境中的 Python 解释器，确保包被安装到虚拟环境中。

### 3. **安装路径**

- **`pip install`**：
  - 在全局环境中，包安装到`/usr/local/lib/python3.x/site-packages`或类似路径。
  - 在虚拟环境中，包安装到虚拟环境的`lib/python3.x/site-packages`目录。
- **`./.venv/bin/python -m pip install`**：
  - 包始终安装到指定的虚拟环境的`lib/python3.x/site-packages`目录。

### 4. **依赖项安装**

- **`pip install`**：
  - 会自动安装依赖项，但依赖项的安装路径取决于当前环境。
- **`./.venv/bin/python -m pip install`**：
  - 也会自动安装依赖项，但所有依赖项都会安装到指定的虚拟环境中。

### 5. **版本冲突**

- **`pip install`**：
  - 如果全局环境和虚拟环境中存在版本冲突，可能会导致问题。
- **`./.venv/bin/python -m pip install`**：
  - 由于明确指定了虚拟环境，可以避免版本冲突。

### 6. **安装选项**

- **`pip install`**：
  - 可以使用`--user`选项将包安装到用户目录，而不是全局目录。
  - 可以使用`--target`选项指定安装路径。
- **`./.venv/bin/python -m pip install`**：
  - 通常不需要额外选项，因为路径已经明确指定。

### 7. **示例**

- **全局环境**：

  ```bash
  pip install requests
  ```

  这会将`requests`包安装到全局环境中。

- **虚拟环境（未激活）**：

  ```bash
  ./.venv/bin/python -m pip install requests
  ```

  这会将`requests`包安装到`.venv`虚拟环境中。

- **虚拟环境（已激活）**：
  ```bash
  source ./.venv/bin/activate
  pip install requests
  ```
  这会将`requests`包安装到已激活的虚拟环境中。

### 8. **总结**

- **`pip install`**：适用于简单场景，特别是在虚拟环境已激活的情况下。
- **`./.venv/bin/python -m pip install`**：适用于需要明确指定虚拟环境路径的场景，特别是在虚拟环境未激活时。

选择哪种方式取决于你的具体需求和使用场景。如果需要确保包安装到特定的虚拟环境中，建议使用`./.venv/bin/python -m pip install`。

## 使用 `lxml` 和 `BeautifulSoup` 解析 HTML 时，它们有一些明显的异同：

### 相同点：

1. **目的相同**：两者都用于解析 HTML 和 XML 文档，并从中提取数据。
2. **灵活性**：都可以处理不规范的 HTML 文档，具有一定的容错性。

### 不同点：

1. **性能**：

   - `lxml` 是基于 C 语言开发的，因此解析速度更快，尤其在处理大型文档时性能更优。
   - `BeautifulSoup`（BS4）虽然功能强大，但相比于 `lxml`，解析速度较慢。

2. **解析器选项**：

   - `BeautifulSoup` 允许用户选择不同的解析器，如 `html.parser`、`lxml`、`html5lib`，这提供了更多的灵活性。
   - `lxml` 本身作为一个解析器，不提供选择其他解析器的选项。

3. **易用性和学习曲线**：

   - `BeautifulSoup` 的 API 设计简单直观，适合初学者，易于理解和使用。
   - `lxml` 的 API 相对复杂，尤其是涉及到 XPath 和 XSLT 时，学习曲线较陡。

4. **容错性**：

   - `BeautifulSoup` 在处理不规范 HTML 时表现出色，能够自动修复一些文档错误。
   - `lxml` 虽然也有一定的容错能力，但不如 `BeautifulSoup` 强大。

5. **功能扩展性**：

   - `lxml` 提供了 XPath 和 CSS 选择器等更强大的功能，适合复杂的数据抽取操作。
   - `BeautifulSoup` 提供了丰富的搜索功能和多种选择器，但相对 `lxml` 来说功能扩展性稍弱。

6. **社区和文档**：

   - `BeautifulSoup` 拥有一个非常活跃的社区和丰富的学习资源，适合新手开发者。
   - `lxml` 社区相对稳定，但资源和示例可能不如 `BeautifulSoup` 丰富。

7. **安装和依赖**：
   - `BeautifulSoup` 可以单独使用，也可以与 `lxml` 等解析器结合使用，而 `lxml` 需要单独安装，且在某些系统上安装可能较为复杂。

总结来说，如果你需要处理大型或复杂的文档，并且对性能有较高要求，`lxml` 可能是更好的选择。而如果你是 HTML 解析的新手，或者需要一个错误处理能力强、易于上手的库，`BeautifulSoup` 可能更适合你。在实践中，两者也可以结合使用，利用 `BeautifulSoup` 的易用性和 `lxml` 的高性能。

## await session.get()和 async with session.get()区别：

### 总结

- **`await session.get()`**：适合简单的请求，直接返回响应对象，但需要手动管理资源。
- **`async with session.get()`**：适合需要明确管理资源的场景，确保响应对象在使用完毕后自动关闭，避免资源泄漏。

根据具体需求选择合适的写法。如果需要更安全的资源管理，建议使用 `async with session.get()`。

### 区别解释

#### 1. **语法结构**

- **`await session.get()`**：

  - 直接使用 `await` 关键字调用 `session.get()` 方法，返回一个 `ClientResponse` 对象。
  - 适合简单的请求，不需要额外的上下文管理。
  - 示例：
    ```python
    result = await session.get(url, cookies=cookies, timeout=10, allow_redirects=False)
    ```

- **`async with session.get()`**：
  - 使用异步上下文管理器 `async with`，确保在请求完成后自动关闭响应对象，释放资源。
  - 更适合需要明确管理资源的场景，特别是在处理重定向或需要确保资源正确释放时。
  - 示例：
    ```python
    async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
        # 处理响应
    ```

#### 2. **资源管理**

- **`await session.get()`**：

  - 需要手动管理响应对象的生命周期，例如在使用完毕后关闭响应。
  - 如果忘记关闭响应对象，可能会导致资源泄漏。

- **`async with session.get()`**：
  - 自动管理响应对象的生命周期，确保在上下文块结束后自动关闭响应对象。
  - 更安全，避免资源泄漏。

#### 3. **参数设置**

- **`cookies`**：

  - 在 `await session.get()` 中，`cookies` 参数用于设置请求的 Cookie。
  - 示例：
    ```python
    result = await session.get(url, cookies=cookies, timeout=10, allow_redirects=False)
    ```

- **`proxy`**：
  - 在 `async with session.get()` 中，`proxy` 参数用于设置代理服务器。
  - 示例：
    ```python
    async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
        # 处理响应
    ```

#### 4. **超时设置**

- **`timeout`**：
  - 两个方法都可以设置 `timeout` 参数，用于指定请求的超时时间。
  - 示例：
    ```python
    result = await session.get(url, timeout=10)
    async with session.get(url, timeout=15) as response:
        # 处理响应
    ```

#### 5. **重定向处理**

- **`allow_redirects`**：
  - 两个方法都可以设置 `allow_redirects` 参数，用于控制是否允许自动重定向。
  - 示例：
    ```python
    result = await session.get(url, allow_redirects=False)
    async with session.get(url, allow_redirects=False) as response:
        # 处理响应
    ```
