// Lino José Comesaña Cebral
// Técnicas de análise e simulación en Física Nuclear e de Partículas. Máster en Física, curso 2019/2020.


// Nesta macro de C++ imos abrir o histograma que creamos coas simulacións e mostrar en
// pantalla 2 canvas: un co histograma tal cal e outro con dous plots correspondentes ás
// proxeccións nos eixos X e Y onde teñamos o cursor (sobre o canvas co histograma prin-
// cipal).



// Variable de texto que porei sobre o meu Canvas, só por cuestións de estética:
TText *info;

// Unha variable que empregarei máis adiante:
TH2* readThis = 0;

// Abrimos o arquivo onde temos o histograma en 2D (TH2D):
TFile* ARQUIVO = TFile::Open("histograma.root");

// Constrúo a miña función proba():

void proba()
{
   auto Canvas = new TCanvas("Canvas", "Canvas", 0, 0, 500, 500); // Creamos o Canvas
   TString hname="nombre"; // Variable de texto que empregarei máis adiante...
   TH1F *h2 = (TH1F*) ARQUIVO->Get(hname); // Collemos o histograma do .root que abrimos antes e o almacenamos coa variable h2
   h2->Draw("col Z"); // Debuxo o histograma coa barra de cores á dereita

   // Creo a etiqutea de texto que definín xusto antes de comezar o void{}:
   info = new TText(0.0, 22.5, "Move o cursor sobre o histograma");
   info->SetTextAlign(22);
   info->SetTextSize(0.04);
   info->SetTextColor(kRed+1);
   info->SetBit(kCannotPick);

   // Engado a etiqueta ao Canvas e actualizoo:
   info->Draw();
   Canvas->Update();

   // Fago que as filas e columnas do histograma poidan ser seleccionadas/resaltadas (este é o principio de funcionamento de todo)
   h2->SetHighlight();

   // O Canvas cando detecta o cursor sobre unha fila ou columna xera un sinal 
   Canvas->HighlightConnect("Highlight2(TVirtualPad*,TObject*,Int_t,Int_t)");
}




// Imos definir agora unha función que faga:
//   1) Crear as proxeccións nos eixos X e Y do histograma coma se fosen histogramas do tipo TH1.
//   2) Detectar o cursor sobre algún bin e actualice directamente os dous plots das proxeccións.

void Highlight2(TVirtualPad *pad, TObject *obj, Int_t xhb, Int_t yhb);


void Highlight2(TVirtualPad *pad, TObject *obj, Int_t xhb, Int_t yhb)
{
   auto h2 = (TH2F *)obj;
   if(!h2) return;
   auto CanvasProxeccion = (TCanvas *) gROOT->GetListOfCanvases()->FindObject("CanvasProxeccion"); // Atopamos a Proxección vixente (de habela, se acabamos de iniciar o programa non haberá algunha e o seu valor será null).
   if (!h2->IsHighlight()) { // No momento no cal RESÁLTASE algunha zona do histograma...
      if (CanvasProxeccion) delete CanvasProxeccion; // Destruímos a proxección anterior e preparámonos para crear a nova.
      return;
   }

   info->SetTitle(""); // Para borrar a etiqueta

   auto fila_x = h2->ProjectionX("Proxeccion_en_x", yhb, yhb); // Plot da proxección no eixo X
   auto columna_y = h2->ProjectionY("Proxeccion_en_y", xhb, xhb); // Plot da proxección no eixo Y
   fila_x->SetTitle(TString::Format("Proxeccion do bin[%02d] na direccion X", yhb)); // Título da proxección horizontal
   columna_y->SetTitle(TString::Format("Proxeccion do bin[%02d] na direccion Y", xhb)); // Título da proxección vertical

   // Cando movemos o cursor sobre o histograma invocamos un novo Canvas: CanvasProxeccion
   if (!CanvasProxeccion) {
      CanvasProxeccion = new TCanvas("CanvasProxeccion", "CanvasProxeccion", 505, 0, 600, 600);
      CanvasProxeccion->Divide(1, 2); // Dividimos o Canvas en dous Pads ou canles para cada proxección
      CanvasProxeccion->cd(1); // Movémonos á canle 1...
      fila_x->Draw(); // e debuxamos nela a proxección do eixo X
      CanvasProxeccion->cd(2); // Movémonos agora á canle 2...
      columna_y->Draw(); // e debuxamos nela a proxección do eixo Y
   }

   // Actualizamos o CanvasProxeccion global
   CanvasProxeccion->GetPad(1)->Modified();
   CanvasProxeccion->GetPad(2)->Modified();
   CanvasProxeccion->Update();
}
