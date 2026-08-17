# claude-usage-statusline

Claude Code 用プラグインのマーケットプレイスリポジトリ。

Claude Code のステータスラインに、公式のプラン使用制限（5時間 / 7日ウィンドウ）を
プログレスバーで表示する `usage-statusline` プラグインを配布します。

```
🤖 Fable 5 | 🟢 5h [█░░░░░░░░░] 10%使用済み (残り3時間38分 / 14:30リセット) | 🟢 7d [███░░░░░░░] 26%使用済み (残り15時間8分 / 08/18 02:00リセット)
```

## インストール

```
/plugin marketplace add toshikidev821/claude-usage-statusline
/plugin install usage-statusline@toshikidev821-plugins
```

インストール後、`/usage-statusline:install` を実行するとステータスラインが設定されます。
