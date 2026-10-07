# Frederik Pedersen · Akademisk portfolio

Dansk portfolio bygget med **C# og Blazor WebAssembly på .NET 10**. Filtrering sker i Blazor; projektbeskrivelser kan foldes ud. Responsivt design med tastaturnavigation og reduceret bevægelse.

## Start i VS Code

Installér .NET 10 SDK. Åbn mappen, og kør:

```sh
dotnet restore --locked-mode
dotnet run
```

Åbn localhost-adressen fra terminalen. Redigér personlige tekster i `Home.razor`, projekter i `Data/ProjectCatalog.cs` og design i `wwwroot/css/app.css`. `Data/projects.json` er en dokumentationskopi, som skal opdateres sammen med kataloget. Der er ikke indsat opdigtede repository-links, rapporter, e-mail eller portrætfoto. GitHub-linket bruger fktp; kontrollér det før offentliggørelse. Projektbeskrivelserne omtaler gruppeprojekter uden at påstå, at alt er lavet individuelt.

## Pipeline fra opgaven

| Krav | Implementering | Aktivering |
| --- | --- | --- |
| Offentligt repo | Projektet er klart til upload | Opret et nyt public GitHub-repo |
| Push til main går live | Azure Static Web Apps deploy efter checks | Opret Azure-site og repository-secret |
| Preview pr. PR | Azure preview og automatisk oprydning | Understøtter PR fra branches i samme repo |
| Mindst to deterministiske CI-trin | Build med warnings som fejl + kontrakt- og risikotests | GitHub Actions |
| Probabilistisk CI | Read-only AI-review af PR-diff | Aktivér GitHub Models for repoet |
| Beskyttet main | Required checks og menneskeligt review | Sæt GitHub branch rules manuelt |
| README om pipeline | Dette dokument | Inkluderet |
| Risk level | LOW / MEDIUM / HIGH i Actions summary | Inkluderet |

AI-reviewet er rådgivende. Det kører separat fra deployment og er ikke en sikkerhedsgaranti. API-fejl giver et fejlet review-job, ikke et opdigtet review. Output står i Actions-jobbets summary. Diff er afgrænset til 18.000 tegn med synlig besked om afkortning. Ingen agent kan køre kommandoer eller merge. Fork-PR får CI, men ingen deployment-secrets og dermed ingen automatisk preview; lav en betroet branch i repoet, hvis opgavens alle-PR-previewkrav skal dækkes. GitHub Models kan være begrænset af kontoens adgang og kvoter.

## Gør den live

1. Opret et **nyt offentligt GitHub-repository** og upload hele mappen inklusive `.github`. Brug ikke guest-lecture-repoet som portfolio-repo.
2. Opret en Azure Static Web App med dette repo og `main` som produktionsbranch. Vælg en plan efter behov; kontrollér pris og kontoopsætning inden oprettelse. Brug det medfølgende workflow frem for et ekstra autogenereret workflow.
3. Læg deployment-tokenet i repository-secreten `AZURE_STATIC_WEB_APPS_API_TOKEN`. Aktivér GitHub Models i repoets indstillinger.
4. Under Settings → Rules → Rulesets: beskyt `main`, kræv pull request, mindst én godkendelse, `checks` som required status check, og blokér force-push/deletion. Aktivér først required check efter den første kørsel, så det kan vælges. HIGH kræver ekstra menneskeligt review som beskrevet i risikopolitikken; scriptet håndhæver ikke selv antallet af reviewers.
5. Lav en PR fra en branch i samme repo. Kontrollér build, tests, AI-summary og preview-link. Merge giver produktion-deployment.

Azure kræver en konto og deployment-token. Repository og hosting er **ikke oprettet** ved at downloade dette projekt. Der er ingen fungerende live-URL, før opsætningen er gennemført.

## Lokale checks

```sh
python3 -m unittest discover -s tests -v
dotnet build --no-restore --configuration Release -warnaserror
dotnet publish --no-restore --configuration Release --output artifacts/publish
```

Dependencyversioner og SDK feature band er angivet. Efter en tilsigtet dependencyopdatering: `dotnet restore --force-evaluate`, commit den opdaterede `packages.lock.json`. CI bruger locked restore for at opdage utilsigtede ændringer. SDK tillader patchopdateringer. Action-tags og runner-image er ikke immutable; pin actions til verificerede commit-SHA’er, hvis undervisningens CI-kit kræver det.

## Indhold og sikkerhed

Portfolien har ingen database, login eller kontaktformular. Ingen secrets må ligge i klientkode: Blazor WebAssembly downloades til besøgendes browser. Hostingkonfigurationen inkluderer sikkerhedsheaders og navigation fallback. CSP skal verificeres mod den deployede .NET-runtime i browseren. Test mobilvisning, tastatur, filtre, projektudfoldelse og genindlæsning på den faktiske host før aflevering.

Den viste risikopolitik er en selvstændig regel inspireret af billedet; den er ikke udgivet som din originale regel fra exercise 04. CI-kit fra undervisningen er ikke importeret.

## Verificering ved levering

Syv Python-tests består, workflowets YAML kan parses, og .NET restore har genereret lock-filen. Release-build blev forsøgt med .NET 10.0.100, men stoppede med MSB4216 / MSB4027 i ComputeWasmBuildAssets: miljøets MSBuild taskhost kunne ikke oprettes. Derfor er Blazor-build, browservisning, AI-API-kald og deployment ikke verificeret. Kør kommandoerne ovenfor på din egen maskine inden aflevering.
