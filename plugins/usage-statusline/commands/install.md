---
description: 使用率ステータスラインをユーザーの settings.json に設定する
---

このプラグインに同梱されたステータスラインスクリプトを、ユーザーの Claude Code に設定してください。

手順:

1. プラグインのスクリプトをユーザーのスクリプト置き場にコピーする（プラグイン更新でキャッシュパスが変わっても壊れないようにするため）:

```bash
mkdir -p ~/.claude/scripts
cp "${CLAUDE_PLUGIN_ROOT}/scripts/token_usage_statusline.py" ~/.claude/scripts/token_usage_statusline.py
```

2. `~/.claude/settings.json` を読み、`statusLine` キーを次の内容に設定する（他のキーは変更しない）:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/scripts/token_usage_statusline.py",
    "refreshInterval": 5
  }
}
```

3. 設定後、ステータスラインの表示例をユーザーに伝える:

```
🤖 Fable 5 | 🟢 5h [█░░░░░░░░░] 10%使用済み (残り3時間38分 / 14:30リセット) | 🟢 7d [███░░░░░░░] 26%使用済み (残り15時間8分 / 08/18 02:00リセット)
```

注意:

- 既に `statusLine` が設定されている場合は、上書きしてよいかユーザーに確認すること。
- `settings.json` が存在しない場合は `statusLine` キーだけを持つ JSON を新規作成すること。
