namespace Portfolio.Data;
public sealed record AcademicProject(string Id, string Title, string Category, string Number, string Subtitle, string Summary, string Work, string Learning, string[] Tags);
public static class ProjectCatalog
{
    public static IReadOnlyList<AcademicProject> All { get; } =
    [
        new("pharma", "P4Pharma", "Sikkerhed", "01", "Sikkerhed i en applikation til farmaceutisk arbejde", "En intern webapplikation til upload af logs og testresultater, hvor adgang til data afhænger af brugerens rolle.", "Projektet omfattede login med TOTP, rollebaseret adgang og kontrol af, hvem der havde oprettet en sag. Sikkerhedsarbejdet tog udgangspunkt i SQL injection, XSS og Broken Access Control.", "Jeg arbejdede med sammenhængen mellem authentication og authorization: At kunne logge ind er ikke det samme som at have adgang til alle data.", ["Blazor", "ASP.NET Core", "MySQL", "OWASP"]),
        new("games", "SpilSøgningsPortal", "Udvikling", "02", "Eksterne API’er møder en Blazor-applikation", "En webapplikation, der kombinerer information fra Steam og CheapShark med login og en SQL-database.", "Semesterprojektet kombinerede API-integration, databasedesign og brugerlogin. Data fra forskellige tjenester skulle indgå i én samlet applikation.", "Jeg fik erfaring med at forbinde en brugergrænseflade, eksterne datakilder og en database og med at håndtere de forskellige datastrukturer.", ["C#", "Blazor", "REST API", "SQL"]),
        new("robot", "Autonom robot", "Robotik", "03", "Navigation, sensorer og et digitalt kort", "Et robotprojekt med ruteplanlægning på et grid, kamerabehandling og overførsel af sensordata til en webapplikation.", "Projektet brugte JetBot / Jetson Nano, Arduino MKR WiFi 1010, MQ-4 og MQ-135. D* Lite planlagde ruter på et 20 × 20 grid, mens UDP forbandt dele af systemet.", "Jeg arbejdede med et system, hvor software skulle reagere på en fysisk verden. Gasværdierne var grove sensorestimater og ikke præcist kalibrerede ppm-målinger.", ["D* Lite", "OpenCV", "Arduino", "UDP"]),
    ];
    public static IEnumerable<AcademicProject> Filter(string category) =>
        category == "Alle" ? All : All.Where(p => p.Category == category);
}
