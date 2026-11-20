# Aplicativos Android e iOS

Os dois aplicativos embutem a simulação (`www/index.html`) em uma WebView nativa, via [Capacitor](https://capacitorjs.com) 8. Funcionam sem internet.

- **Android:** projeto Gradle em `android/` (abre no Android Studio).
- **iOS:** projeto Xcode em `ios/App/App.xcodeproj` (dependências por Swift Package Manager, sem CocoaPods).
- **Identificador:** `io.github.inaciodesa.laboratoriooperante` (troque em `capacitor.config.json` antes de publicar em loja).

## Preparar

```bash
cd mobile
npm install
```

## Rodar

```bash
npm run android   # atualiza o conteúdo e abre o Android Studio
npm run ios       # atualiza o conteúdo e abre o Xcode
```

No Android Studio ou no Xcode, escolha um aparelho ou emulador e clique em Run. Para instalar em um iPhone real, selecione o seu time em Signing & Capabilities.

## Atualizar o conteúdo

Depois de editar o `index.html` da raiz, rode `npm run sync`. Ele regenera `www/index.html` e copia para os dois projetos nativos.

## Nos aplicativos

- "Salvar ponto" guarda o rato no armazenamento do aplicativo.
- "Baixar arquivo" abre a folha de compartilhamento do sistema quando o aparelho oferece esse recurso.
