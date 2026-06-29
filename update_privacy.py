import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('en/*.html')
# exclude ref.html and ref2.html
html_files = [f for f in html_files if not f.startswith('ref')]

new_modal_content = """<!-- Privacy Policy Modal -->
    <div id="privacy-modal" class="fixed inset-0 z-[100] hidden items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="bg-white w-full max-w-4xl max-h-[95vh] overflow-hidden flex flex-col relative shadow-2xl rounded-sm">
            <!-- Close Button -->
            <button onclick="closePrivacyModal()" class="absolute top-4 right-4 text-gray-400 hover:text-brand-orange transition-colors z-50">
                <i class="fas fa-times text-2xl"></i>
            </button>
            
            <!-- Modal Content -->
            <div class="p-8 md:p-12 overflow-y-auto custom-scrollbar">
                <div class="max-w-3xl mx-auto">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-10 h-[2px] bg-brand-orange"></div>
                        <span class="text-brand-orange font-bold uppercase tracking-[0.2em] text-xs">Cumplimiento Legal</span>
                    </div>
                    <h2 class="text-2xl md:text-3xl font-black text-brand-dark uppercase tracking-tight mb-8 border-b border-gray-100 pb-6">
                        AVISO DE PRIVACIDAD<br>
                        <span class="text-lg md:text-xl text-gray-400">PARA CLIENTES Y PROVEEDORES</span>
                    </h2>
                    
                    <div class="space-y-6 text-gray-600 leading-relaxed text-sm md:text-base">
                        <p><strong>INGENIERÍA AVANTE DE OCCIDENTE S.A. DE C.V.</strong> con domicilio en Avenida del Cobre No. 8, Col. El Castillo, El Salto, Jalisco, de conformidad con lo dispuesto en la Ley Federal de Protección de Datos Personales en Posesión de los Particulares hace de su conocimiento el presente Aviso de Privacidad para los clientes y proveedores:</p>

                        <div class="bg-gray-50 p-6 border-l-4 border-brand-orange">
                            <h3 class="font-black uppercase text-brand-dark mb-3 tracking-wide text-sm">SOBRE EL TRATAMIENTO DE SUS DATOS PERSONALES DE LOS CLIENTES Y PROVEEDORES:</h3>
                            <p class="text-sm">Recabamos sus datos personales y datos personales sensibles para los efectos mencionados en el presente Aviso de Privacidad. En éste sentido, hacemos de su conocimiento que sus datos personales serán tratados y resguardados con base en los principios de licitud, calidad, consentimiento, información, finalidad, lealtad, proporcionalidad y responsabilidad, consagrados en la Ley Federal de Protección de Datos Personales en Posesión de los Particulares.</p>
                        </div>

                        <div>
                            <h3 class="font-black uppercase text-brand-dark mb-3 tracking-wide text-sm">FINALIDAD EN EL TRATAMIENTO DE SUS DATOS PERSONALES:</h3>
                            <p>Recopilamos sus datos personales y datos personales sensibles por lo que solicitamos su consentimiento a través del presente Aviso de Privacidad con el objeto de utilizarlos para los siguientes fines:</p>
                            <ul class="list-none pl-0 mt-4 space-y-3">
                                <li class="flex gap-2"><span class="font-bold text-brand-orange">I.</span> Para contactarlo y enviarle información relevante sobre nuestros productos.</li>
                                <li class="flex gap-2"><span class="font-bold text-brand-orange">II.</span> Identificarlo como cliente y/o proveedor de INGENIERÍA AVANTE DE OCCIDENTE S.A. DE C.V.</li>
                                <li class="flex gap-2"><span class="font-bold text-brand-orange">III.</span> Para realizar todas las gestiones internas necesarias relacionadas con la relación comercial vigente, incluyendo cuestiones de crédito y pagos.</li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="font-black uppercase text-brand-dark mb-3 tracking-wide text-sm">MEDIOS PARA LIMITAR EL USO O DIVULGACIÓN DE SUS DATOS PERSONALES:</h3>
                            <p>Hacemos de su conocimiento que sus datos personales y datos personales sensibles serán resguardados bajo estrictas medidas de seguridad administrativas, técnicas y físicas las cuales han sido implementadas con el objeto de proteger sus datos personales contra daño, pérdida, alteración, destrucción o el uso, acceso o tratamiento no autorizados.</p>
                        </div>

                        <div class="border border-gray-100 p-6 rounded-sm">
                            <h3 class="font-black uppercase text-brand-dark mb-3 tracking-wide text-sm">MEDIOS PARA EL EJERCICIO DE SUS DERECHOS COMO TITULAR DE LOS DATOS PERSONALES:</h3>
                            <p>Como titular de los datos personales objeto del presente Aviso de Privacidad usted podrá ejercitar sus derechos de acceso, rectificación, cancelación u oposición (Derechos ARCO), mismos que se consagran en la Ley Federal de Protección de Datos Personales en Posesión de los Particulares. Así mismo podrá revocar el consentimiento otorgado para el uso de sus datos personales. En cualquiera de estos supuestos, puede realizar su solicitud mediante el envío de un correo electrónico a la dirección <a href="mailto:aprivacidad@iao.com.mx" class="text-brand-orange hover:underline font-bold">aprivacidad@iao.com.mx</a></p>
                            <p class="mt-4 text-[11px] text-gray-400 italic">Con la finalidad de poder atender su solicitud, ésta deberá satisfacer todos los requisitos estipulados en la Ley Federal de Protección de Datos Personales en Posesión de los Particulares.</p>
                        </div>

                        <div>
                            <h3 class="font-black uppercase text-brand-dark mb-3 tracking-wide text-sm">TRANSFERENCIA DE SUS DATOS PERSONALES</h3>
                            <p>Sus datos personales y/o datos personales sensibles podrán ser transferidos a los terceros, que para el cumplimiento de las obligaciones que INGENIERÍA AVANTE DE OCCIDENTE S.A. DE C.V. le ofrece, sea necesario. Lo anterior sin perjuicio de las excepciones de la Ley Federal de Protección de Datos Personales en Posesión de los Particulares. Por lo que se solicita su consentimiento expreso para realizar dichas transferencias (Seleccionar sólo 1 opción con una X)</p>
                            <div class="mt-4 space-y-2">
                                <label class="flex items-center gap-3 cursor-pointer group">
                                    <div class="w-5 h-5 border-2 border-brand-orange rounded-sm flex items-center justify-center group-hover:bg-orange-50 transition-colors"></div>
                                    <span class="text-sm font-medium">Doy mi consentimiento para la transferencia de mis datos.</span>
                                </label>
                                <label class="flex items-center gap-3 cursor-pointer group">
                                    <div class="w-5 h-5 border-2 border-brand-orange rounded-sm flex items-center justify-center group-hover:bg-orange-50 transition-colors"></div>
                                    <span class="text-sm font-medium">No doy mi consentimiento para la transferencia de mis datos.</span>
                                </label>
                            </div>
                        </div>

                        <div class="pt-6 border-t border-gray-100">
                            <h3 class="font-black uppercase text-brand-dark mb-3 tracking-wide text-sm">1. CAMBIOS AL PRESENTE AVISO DE PRIVACIDAD</h3>
                            <p>El presente Aviso de Privacidad podrá ser modificado en el futuro. En todo caso, cualquier modificación se publicará en la siguiente página web: <a href="http://www.iao.com.mx" target="_blank" class="text-brand-orange hover:underline font-bold">www.iao.com.mx</a></p>
                            <p class="mt-2 text-sm">Sin embargo, por su seguridad, el Aviso de Privacidad vigente estará disponible en todo momento en la página web antes señalada.</p>
                        </div>

                        <div class="pt-10 space-y-8 opacity-60">
                            <div class="text-center">
                                <p class="font-black uppercase tracking-widest text-brand-dark text-[10px] mb-8">RECIBÍ DE CONFORMIDAD Y DOY MI CONSENTIMIENTO</p>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                                <div class="border-b border-gray-200 pb-2">
                                    <span class="text-[9px] uppercase font-bold text-gray-400 block mb-1">Nombre y Firma</span>
                                    <div class="h-8"></div>
                                </div>
                                <div class="border-b border-gray-200 pb-2">
                                    <span class="text-[9px] uppercase font-bold text-gray-400 block mb-1">Fecha</span>
                                    <div class="h-8"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Footer in modal to acknowledge / close -->"""

import re
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use re.sub to replace everything from <!-- Privacy Policy Modal --> up to <!-- Footer in modal to acknowledge / close -->
    pattern = r'<!-- Privacy Policy Modal -->.*?<!-- Footer in modal to acknowledge / close -->'
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, new_modal_content, content, flags=re.DOTALL)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {fname}")
    else:
        print(f"Skipped {fname} - Pattern not found")
